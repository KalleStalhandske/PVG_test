export interface ExampleData {
  title: string
  body: string
}

export interface TimeEntryOut {
  id: number
  competitor_id: number
  timestamp: string
  station: string
}

export interface TimeEntryIn{
  start_number: string
  station: string;
}

export interface CompetitorOut {
  id: number
  start_number: string
  name: string
}

export interface CompetitorIn {
  start_number: string
  name: string
}