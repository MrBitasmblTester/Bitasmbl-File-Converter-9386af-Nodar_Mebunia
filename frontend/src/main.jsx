import React, {useState} from "react";
import {createRoot} from "react-dom/client";
import "./index.css";
function App(){
  const [task,setTask]=useState(null);
  const [status,setStatus]=useState(null);
  const [download,setDownload]=useState(null);
  async function onUpload(e){
    const f=e.target.files[0]; if(!f) return;
    const fd=new FormData(); fd.append("file", f);
    const res=await fetch("http://localhost:8000/upload",{method:"POST",body:fd});
    const j=await res.json(); setTask(j.task_id); setStatus({status:"queued"});
    const iv=setInterval(async ()=>{ const s=await (await fetch(`http://localhost:8000/status/${j.task_id}`)).json(); setStatus(s); if(s.result){ setDownload(s.result); clearInterval(iv);} },700);
  }
  return (<div className="min-h-screen flex items-center justify-center bg-gray-50">
    <div className="p-6 bg-white rounded shadow w-full max-w-md">
      <h1 className="text-lg font-bold mb-4">File Converter</h1>
      <input type="file" onChange={onUpload} className="mb-3" />
      <div className="text-sm text-gray-600">Status: {status?status.status:"idle"}</div>
      {download? <a className="mt-3 inline-block text-blue-600" href={`http://localhost:8000/download/${download}`}>Download result</a>:null}
    </div>
  </div>);
}
createRoot(document.getElementById("root")||document.body).render(<App/>);
