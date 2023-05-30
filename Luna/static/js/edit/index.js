const getCSRFToken = () => {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : '';
};
const csrfToken = getCSRFToken();

const find_user = async (id) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/users/${id}/`)
            .then((response) => response.json())
            .catch((error) => {
                console.error(error);
            });
        console.log(response);
        return response.detail == 'Not found.' ? false : response;
    } catch (err) {
        console.error(err);
        return false;
    }
};

const searchBtn = document.getElementById('search-btn');
searchBtn.addEventListener('click', async () => {
    const idInput = document.getElementById('id').value;
    if (idInput == '') return;
    data = await find_user(idInput);
    if (!data) {
        console.log('Erro');
    } else {
        document.getElementById('name').value = data.name;
        document.getElementById('email').value = data.email;
        document.getElementById('age').value = data.age;
        document.getElementById('gender').value = data.sex;
    }
});
