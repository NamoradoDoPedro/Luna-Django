const getCSRFToken = () => {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : '';
};

const deleteUser = async (userId) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/users/${userId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
        });
        if (response.ok) {
            alert('DELETE request successful');
        } else {
            console.log(response);
            alert(`DELETE request error: ${response.status}`);
        }
    } catch (err) {
        alert(`DELETE method error: ${err}`);
    }
};

const table = document.getElementById('tbody');

const createButton = (text, className) => {
    const button = document.createElement('button');
    button.innerText = text;
    button.classList.add('btn', className);
    return button;
};

const createUserRow = (user) => {
    const tr = document.createElement('tr');
    table.appendChild(tr);

    tr.innerHTML = `
        <td>${user.id}</td>
        <td>${user.name}</td>
        <td>${user.email}</td>
        <td>${user.age}</td>
        <td>${user.sex}</td>
        <td><button class="btn btn-danger" id="${user.id}">Delete</button></td>
    `;
    document
        .getElementById(`${user.id}`)
        .addEventListener('click', async () => {
            if (confirm(`Do you really want to delete the ID ${user.id}?`)) {
                console.log(`UserID = ${user.id}`);
                try {
                    await deleteUser(user.id);
                    location.reload();
                } catch (err) {
                    alert(`Error: ${err}`);
                }
            }
        });
};

fetch('http://127.0.0.1:8000/users/')
    .then((response) => response.json())
    .then((users) => {
        users.forEach((user) => createUserRow(user));
    })
    .catch((error) => {
        console.error(error);
    });
