const getCSRFToken = () => {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : '';
};

const find_user = async (id) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/users/${id}/`, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
        })
            .then((response) => response.json())
            .catch(() => {
                return false;
            });
        return response.detail == 'Not found.' ? false : response;
    } catch (err) {
        console.log(`Error in get method: ${err}`);
        return false;
    }
};

const resetForm = () => {
    document.getElementById('name').value = '';
    document.getElementById('email').value = '';
    document.getElementById('age').value = '';
    document.getElementById('sex').value = 'Masculino';
};

const userForm = [
    document.getElementById('name'),
    document.getElementById('email'),
    document.getElementById('age'),
    document.getElementById('sex'),
];

document
    .getElementById('search-btn')
    .addEventListener('click', async (event) => {
        event.preventDefault();
        const idInput = document.getElementById('id').value;
        if (idInput == '') return;
        let data = await find_user(idInput);
        if (!data) {
            resetForm();
            alert('ID not found');
            document.getElementById('edit-btn').setAttribute('disabled', true);
        } else {
            document.getElementById('name').value = data.name;
            document.getElementById('email').value = data.email;
            document.getElementById('age').value = data.age;
            if (data.sex == 'Outro') {
                document.getElementById('sex').value = 'Outro';
            } else {
                document.getElementById('sex').value =
                    data.sex == 'Masculino' ? 'Masculino' : 'Feminino';
            }
            document.getElementById('edit-btn').removeAttribute('disabled');
        }
    });

document.getElementById('edit-btn').addEventListener('click', async () => {
    for (let i = 0; i < userForm.length; ++i) {
        userForm[i].removeAttribute('disabled');
    }
    document.getElementById('id').setAttribute('disabled', true);
    document.getElementById('search-btn').setAttribute('disabled', true);
    document.getElementById('edit-btn').remove();

    document.getElementById('btn-div').innerHTML = `
        <button id="cancel-btn" class="btn btn-danger" onClick="location.reload()" type="reset">Cancel</button>
        <button id="confirm-btn" class="btn btn-primary" type="submit">Confirm</button>
    `;

    document.getElementById('cancel-btn').addEventListener('click', () => {
        resetForm();
        document.getElementById('confirm-btn').remove();
        document.getElementById('cancel-btn').remove();
        document.getElementById('btn-div').innerHTML = `
            <button id="edit-btn" class="btn btn-secondary" disabled type="button">Edit</button>
        `;
        for (let i = 0; i < userForm.length; ++i) {
            userForm[i].setAttribute('disabled', true);
        }
        document.getElementById('id').removeAttribute('disabled');
        document.getElementById('search-btn').removeAttribute('disabled');
    });

    document
        .getElementById('confirm-btn')
        .addEventListener('click', async () => {
            const nameInfo = document.getElementById('name').value;
            const emailInfo = document.getElementById('email').value;
            const ageInfo = document.getElementById('age').value;
            const sexInfo = document.getElementById('sex').value;
            const idInput = document.getElementById('id').value;
            data = {
                name: nameInfo,
                email: emailInfo,
                age: formatDate(ageInfo),
                sex: sexInfo,
            };
            try {
                const response = await fetch(
                    `http://127.0.0.1:8000/users/${idInput}/`,
                    {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCSRFToken(),
                        },
                        body: JSON.stringify(data),
                    }
                );
                if (response.ok) {
                    alert('Change request successful');
                } else {
                    alert(`Change request error: ${response.status}`);
                }
            } catch (err) {
                alert(`Change method error: ${err}`);
            }
        });
});

const formatDate = (dateInput) => {
    let dateObj = new Date(dateInput);
    let formatedDate =
        dateObj.getUTCFullYear() +
        '-' +
        ('0' + (dateObj.getUTCMonth() + 1)).slice(-2) +
        '-' +
        ('0' + dateObj.getUTCDate()).slice(-2);
    return formatedDate;
};
