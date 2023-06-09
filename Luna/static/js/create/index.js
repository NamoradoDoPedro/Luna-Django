const getCSRFToken = () => {
    const cookieValue = document.cookie.match(/csrftoken=([^;]+)/);
    return cookieValue ? cookieValue[1] : '';
};

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

const post_user = async (data) => {
    const response = await fetch('http://127.0.0.1:8000/users/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify(data),
    });
    console.log(data);
    if (response.ok) {
        alert('User created successfully!');
    } else {
        alert(`Error status: ${response.status}`);
    }
};

document.getElementById('confirm-btn').addEventListener('click', () => {
    const nameInfo = document.getElementById('name').value;
    const emailInfo = document.getElementById('email').value;
    const ageInfo = document.getElementById('age').value;
    const sexInfo = document.getElementById('sex').value;
    try {
        const data = {
            name: nameInfo,
            email: emailInfo,
            age: formatDate(ageInfo),
            sex: sexInfo,
        };
        if (nameInfo != '' || emailInfo != '' || ageInfo != 'NaN-aN-aN') {
            post_user(data);
        }
    } catch (err) {
        alert(err);
    }
});
