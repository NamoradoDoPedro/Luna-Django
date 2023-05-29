const confirmBtn = document.getElementById('confirm-btn');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function formatDate(dataInput) {
    var dataObj = new Date(dataInput);

    var ano = dataObj.getUTCFullYear();
    var mes = ('0' + (dataObj.getUTCMonth() + 1)).slice(-2);
    var dia = ('0' + dataObj.getUTCDate()).slice(-2);

    var dataFormatada = ano + '-' + mes + '-' + dia;
    return dataFormatada;
}

confirmBtn.addEventListener('click', () => {
    const nameInfo = document.getElementById('name').value;
    const emailInfo = document.getElementById('email').value;
    const ageInfo = formatDate(document.getElementById('age').value);
    const genderInfo = document.getElementById('gender').value;

    if (
        nameInfo != '' ||
        emailInfo != '' ||
        ageInfo != '' ||
        genderInfo != ''
    ) {
        let data = {
            name: nameInfo,
            email: emailInfo,
            age: ageInfo,
            sex: genderInfo,
        };
        fetch('http://127.0.0.1:8000/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(data),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    alert(data.error);
                } else {
                    window.location.reload();
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }
});
