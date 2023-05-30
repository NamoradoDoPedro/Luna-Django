const getCSRFToken = () => {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : '';
};

const deleteUser = async (userId) => {
    const csrfToken = getCSRFToken();
    try {
        const response = await fetch(`http://127.0.0.1:8000/users/${userId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
        });
        if (response.ok) {
            console.log('DELETE request successful');
        } else {
            console.error('DELETE request error:', response.status);
        }
    } catch (error) {
        console.error('DELETE request error:', error);
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
      <td><button class="btn btn-light" data-id="${user.id}">Edit</button></td>
      <td><button class="btn btn-danger" data-id="${user.id}">Delete</button></td>
    `;

    tr.querySelector('.btn-light').addEventListener('click', (event) => {
        const userId = event.target.dataset.id;
    });

    tr.querySelector('.btn-danger').addEventListener('click', async (event) => {
        const userId = event.target.dataset.id;
        const result = confirm(
            `Do you really want to delete the ID ${userId}?`
        );
        if (result) {
            console.log(`UserID = ${userId}`);
            try {
                await deleteUser(userId);
                location.reload();
            } catch (error) {
                console.error(error);
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
