import { useState } from "react"
import { postTimeData } from "../api/api_utils"


export default function Reg() {
    const [idInput, update] = useState("")
    const [timeList, updateTime] = useState([""])
    
    const save =  async () => {
        const res = await postTimeData(idInput) 

        updateTime(l => [res.timestamp.substring(11, 19), ...l])
    }

    return (
        <div>
            <h2> Sida för registrering </h2>
            <text> Skriv in ID nummer i textrutan (XXX), tryck på "Registrera" </text>
            <p></p>
            <label>
                <input name="123" 
                value={idInput} 
                onChange={e => update(e.target.value)}
                className="border border-gray-300 rounded px-3 py-2 text-black bg-white
             focus:outline-none focus:ring-2 focus:ring-blue-500"></input>
            </label>
            <button onClick={save}> Registrera </button>

            <li>{timeList.map(m => <li>{m}</li>)}</li>
        </div>

    )
}