import type { CompetitorOut, TimeEntryIn, TimeEntryOut } from "../types"

export type Method = "GET" | "POST" | "PUT" | "PATCH" |"DELETE";

export class APIError extends Error{
  public status: number;
  public body: unknown;

  constructor(status: number, body: unknown, message = `HTTP ${status}`) {
    super(message);
    this.name = "API Error";
    this.status = status;
    this.body = body;
  }
}

export type APIOptions<B> = {
  method?: Method;
  body?: B;
  headers?: HeadersInit;
  fetchInit?: Omit<RequestInit, "method" | "headers" | "body">;
};

const joinURL = (
  BaseURL: string,
  path: string
): string => path.startsWith("http") ? path : `${BaseURL.replace(/\/+$/, "")}/${path.replace(/^\/+/, "")}`;



// Gets base url
export function getBaseUrl() {
  /*
  const base = process.env.API_BASE_URL;
  if (!base) throw new Error("API_BASE_URL not set");
  return base
  */
 return "http://localhost:8000";
}

export async function api<T = unknown, B = unknown>(path: string, opts?: APIOptions<B>): Promise<T> {
  const BaseURL = getBaseUrl();
  const URL = BaseURL ? joinURL(BaseURL,path) : path;
  const method: Method = opts?.method ?? (opts?.body == undefined ? "GET" : "POST");
  const isFormData: boolean = 
    typeof FormData !== "undefined" && opts?.body instanceof FormData;
  const hasBody = opts?.body !== "undefined" && method !== "GET";
  const headers: HeadersInit = {
    ...(hasBody && !isFormData ? {"Content-Type": "application/json"} : null),
    ...(opts?.headers ?? null)
  }
  const res = await fetch(URL,{
    method,
    headers,
    body: hasBody ? isFormData ? (opts!.body as BodyInit) : JSON.stringify(opts!.body) : undefined,
    ...(opts?.fetchInit ?? null)
  });
  if (res.status === 204 || res.status === 205) return undefined as T;
  const ct = res.headers.get("content-type") ?? "";
  const data: unknown = ct.includes("application/json") ? 
    await res.json().catch(() => undefined) : 
    await res.text().catch(() => undefined);
  if (!res.ok) {
    const msg = 
      typeof(data as {detail?: unknown})?.detail === "string" ?
      (data as {detail: string}).detail :
      `HTTP ${res.status}`;
    throw new APIError(res.status, data, msg);
  }
  return data as T;
}


// Post a new time entry to the API, returns the created TimeEntryOut
export async function postTimeData(startNbr: string): Promise<TimeEntryOut> {
  return api<TimeEntryOut,TimeEntryIn>("/times/record", {
    body: {start_number: startNbr, station: "test"}
  })
}

// Get all time entries from the API
export async function getTimeData(): Promise<TimeEntryOut[]> {
  return api<TimeEntryOut[]>("/times/");
}

// Get time entries by specific ID from the API
export async function getTimeDataById(id: number): Promise<TimeEntryOut[]> {
  return api<TimeEntryOut[]>(`/times/${encodeURIComponent(id)}`);
}


export function getCompetitors(): Promise<CompetitorOut[]> {
  return api<CompetitorOut[]>(`/competitors/`);
}

export function getCompetitorDataById(id: number): Promise<CompetitorOut> {
  return api<CompetitorOut>(`/competitors/${encodeURIComponent(id)}`);
}