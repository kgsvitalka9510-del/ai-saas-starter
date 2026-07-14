import { useState, useEffect } from "react";

export default function Dashboard() {
  const [usage, setUsage] = useState(null);
  
  useEffect(() => {
    fetch("/api/usage")
      .then(r => r.json())
      .then(setUsage);
  }, []);
  
  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <h1 className="text-3xl font-bold mb-8">Dashboard</h1>
      
      <div className="grid grid-cols-3 gap-6">
        <div className="bg-gray-800 p-6 rounded-lg">
          <h2 className="text-gray-400">Total Requests</h2>
          <p className="text-4xl font-bold">{usage?.total_requests || 0}</p>
        </div>
        <div className="bg-gray-800 p-6 rounded-lg">
          <h2 className="text-gray-400">Current Plan</h2>
          <p className="text-4xl font-bold">Free</p>
        </div>
        <div className="bg-gray-800 p-6 rounded-lg">
          <h2 className="text-gray-400">Requests Remaining</h2>
          <p className="text-4xl font-bold">999</p>
        </div>
      </div>
      
      <div className="mt-8 bg-gray-800 p-6 rounded-lg">
        <h2 className="text-xl font-bold mb-4">AI Chat</h2>
        <textarea 
          className="w-full bg-gray-700 rounded p-4"
          placeholder="Ask me anything..."
        />
        <button className="mt-4 bg-blue-600 px-6 py-2 rounded">
          Send
        </button>
      </div>
    </div>
  );
}
