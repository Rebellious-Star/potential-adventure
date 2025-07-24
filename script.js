document.getElementById("adulteration-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(this);

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    const resultDiv = document.getElementById("result");

    if (result.action) {
      resultDiv.innerHTML = `✅ <strong>Recommended Action:</strong> ${result.action}`;
    } else {
      resultDiv.innerHTML = `❌ <strong>Error:</strong> ${result.error}`;
    }
  } catch (error) {
    document.getElementById("result").innerHTML =
      "❌ <strong>Something went wrong. Please try again.</strong>";
  }
});
