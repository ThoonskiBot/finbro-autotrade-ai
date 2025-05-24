
async function fetchAndUpdate(endpoint, elementId) {
    const res = await fetch(endpoint);
    const text = await res.text();
    document.getElementById(elementId).textContent = text;
}

async function fetchStrategies() {
    const res = await fetch("/strategies");
    const data = await res.json();
    const container = document.getElementById("strategy-toggles");
    container.innerHTML = "";
    for (const [strategy, active] of Object.entries(data)) {
        const toggle = document.createElement("button");
        toggle.textContent = strategy + (active ? " ✅" : " ❌");
        toggle.onclick = () => {
            data[strategy] = !active;
            saveStrategies(data);
        };
        container.appendChild(toggle);
    }
}

async function saveStrategies(data) {
    await fetch("/strategies", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    fetchStrategies();
}

async function fetchPnLChart() {
    const res = await fetch("/pnl_data");
    const data = await res.json();

    const ctx = document.getElementById("pnlChart").getContext("2d");
    const chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: data.map(d => d.date),
            datasets: [{
                label: "PnL",
                data: data.map(d => d.pnl),
                fill: false,
                borderColor: "lime",
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            animation: false
        }
    });
}

function refreshDashboard() {
    fetchAndUpdate("/summary", "summary");
    fetchAndUpdate("/logs", "log");
    fetchStrategies();
    fetchPnLChart();
}

setInterval(refreshDashboard, 3000);
refreshDashboard();
