import React, { useState } from 'react'
export default function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [userId] = useState(() => 'user-' + Math.random().toString(36).slice(2,9))
  const [sessionId] = useState(() => 'sess-' + Math.random().toString(36).slice(2,9))
  const API_BASE = window.__API_BASE__ || ''
  async function send() {
    if(!input.trim()) return
    const userMsg = { role: 'user', text: input }
    setMessages(m => [...m, userMsg])
    setInput('')
    try {
      const res = await fetch((API_BASE || '') + '/interact', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ user_id: userId, session_id: sessionId, input })
      })
      const data = await res.json()
      const aiText = data.llm_response || JSON.stringify(data.action_results || data)
      setMessages(m => [...m, { role: 'assistant', text: aiText }])
    } catch (e) {
      setMessages(m => [...m, { role:'system', text: 'Error: ' + e.message }])
    }
  }
  async function sendFeedback(rating) {
    try {
      await fetch((API_BASE || '') + '/feedback', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ session_id: sessionId, rating })
      })
      alert('Thanks for the feedback!')
    } catch (e) {
      alert('Feedback failed: ' + e.message)
    }
  }
  return (
    <div className="app">
      <header>
        <h1>Agentic Productivity Helper</h1>
        <p>Session: {sessionId}</p>
      </header>
      <main>
        <div className="chat-window">
          {messages.map((m, i) => (
            <div key={i} className={`msg ${m.role}`}>
              <div className="role">{m.role}</div>
              <div className="text">{m.text}</div>
            </div>
          ))}
        </div>
        <div className="controls">
          <input value={input} onChange={e=>setInput(e.target.value)} placeholder="Type a request (e.g., schedule meeting with Alex tomorrow 3pm)" />
          <button onClick={send}>Send</button>
          <div className="feedback">
            <button onClick={()=>sendFeedback(5)}>👍</button>
            <button onClick={()=>sendFeedback(1)}>👎</button>
          </div>
        </div>
      </main>
      <footer>Powered by LangGraph + LiteLLM (configurable)</footer>
    </div>
  )
}
