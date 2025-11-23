async function askAI() {
    const question = document.getElementById("user-question").value;

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await res.json();

        // Display answer in chat.html
        document.getElementById("ai-response").textContent = data.answer;

        // Send coords and recent_news to index.html (example: localStorage or global event)
        localStorage.setItem("incident_coords", JSON.stringify(data.coords));
        localStorage.setItem("recent_news", JSON.stringify(data.recent_news));

        console.log("Coords and news stored for index.html:", data.coords, data.recent_news);
    } catch (err) {
        console.error("Fetch error:", err);
    }
}
