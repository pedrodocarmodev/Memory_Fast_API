const BASE_URL = "http://localhost:8000/training";

let currentTrainingId = null;

const createForm = document.getElementById("createForm");
const answerForm = document.getElementById("answerForm");

const trainingArea = document.getElementById("trainingArea");
const resultArea = document.getElementById("resultArea");

const providedInput = document.getElementById("provided");
const sequenceBox = document.getElementById("sequenceBox");

let hidden = false;

providedInput.addEventListener("focus", () => {
    if (!hidden) {
        sequenceBox.classList.add("d-none");
        hidden = true;
    }
});


createForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    sequenceBox.classList.remove("d-none");
    document.getElementById("provided").value = "";

    hidden = false;

    const user_id = parseInt(document.getElementById("user_id").value);
    const category = document.getElementById("category").value;
    const length = parseInt(document.getElementById("length").value);

    try {
        const response = await fetch(`${BASE_URL}/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id, category, length })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(JSON.stringify(data));
        }

        currentTrainingId = data.id;

        document.getElementById("sequenceBox").textContent = data.sequence;

        trainingArea.classList.remove("d-none");
        resultArea.classList.add("d-none");

    } catch (error) {
        alert("Erro ao criar treino.");
        console.error(error);
    }
});

answerForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const provided = document.getElementById("provided").value;

    try {
        const response = await fetch(`${BASE_URL}/${currentTrainingId}/answer`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ provided })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(JSON.stringify(data));
        }

        const resultBox = document.getElementById("resultBox");

        if (data.correct) {
            resultBox.className = "alert alert-success";
            resultBox.innerHTML = `
                ✅ Correto!<br>
                Esperado: <strong>${data.expected}</strong><br>
                Enviado: <strong>${data.provided}</strong>
            `;
        } else {
            resultBox.className = "alert alert-danger";
            resultBox.innerHTML = `
                ❌ Errado!<br>
                Esperado: <strong>${data.expected}</strong><br>
                Enviado: <strong>${data.provided}</strong>
            `;
        }

        resultArea.classList.remove("d-none");

    } catch (error) {
        alert("Erro ao enviar resposta.");
        console.error(error);
    }
});

