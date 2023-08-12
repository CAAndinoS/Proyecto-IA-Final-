// Función para validar el formulario antes de enviarlo
function submitForm(event) {
    event.preventDefault();

    // Validar que los campos no estén vacíos antes de enviar el formulario
    const formData = new FormData(event.target);
    const values = Object.fromEntries(formData.entries());
    const fields = Object.keys(values);
    const emptyFields = fields.filter(field => !values[field].trim());

    if (emptyFields.length > 0) {
        alert("Por favor, complete todos los campos antes de enviar el formulario.");
        return;
    }

    // Validar que los campos numéricos contengan valores válidos
    const numericFields = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level'];
    const invalidNumericFields = numericFields.filter(field => isNaN(values[field]));

    if (invalidNumericFields.length > 0) {
        alert("Por favor, ingrese valores numéricos válidos en los campos correspondientes.");
        return;
    }

    // Si todos los campos están completos y los campos numéricos son válidos, procedemos con el envío del formulario
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  // Parsear la respuesta JSON
    .then(data => {
        // Almacenar el resultado en el localStorage
        localStorage.setItem('predictionResult', data.result);

        // Redirigir a la página result.html
        window.location.href = '/result';
    })
    .catch(error => console.error('Error:', error));
}

// Asociar la función de validación al evento de envío del formulario
document.getElementById("diagnosis-form").addEventListener("submit", submitForm);
