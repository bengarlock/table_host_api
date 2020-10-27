const usersUrl = "http://127.0.0.1:8000/books/"
const userContainer = document.getElementById("users-container")

const defaultUser = {
    username: '',
    password: '',
    first_name: '',
    last_name: '',
    address: '',
    city: '',
    state: ''
}

document.addEventListener("DOMContentLoaded", e => {

    const renderUsers = () => {
        userContainer.innerHTML = ''
        fetch(usersUrl)
            .then(res=> res.json())
            .then(users => users.forEach(user => renderUser(user)))
    }

    const renderUser = (user) => {
        const userDiv = document.createElement("div")
        userDiv.dataset.id = user.id
        userDiv.dataset.username = user.username
        userDiv.dataset.password = user.password
        userDiv.dataset.first_name = user.first_name
        userDiv.dataset.last_name = user.last_name
        userDiv.dataset.address = user.address
        userDiv.dataset.city = user.city
        userDiv.dataset.state = user.state
        userDiv.innerHTML = `
        <p>${user.first_name}</p>      
        <button>Update</button>  
        <button>Delete</button>
        `
        userContainer.append(userDiv)
    }

    const submitHandler = () => {
        document.addEventListener("submit", e => {
            e.preventDefault()
            if (e.target.id === "new-user-form"){
                const button = e.target
                submitUserForm(button)
            }
        })
    }

    const clickHandler = () => {
        document.addEventListener("click", e => {
            if (e.target.innerText === "Delete") {
                deleteUser(e.target)
            } else if (e.target.innerText === "Update") {
                renderUpdateUserForm(e.target)
            } else if (e.target.innerText === "Update User") {
                updateUser(e.target)
            }
        })
    }

    const submitUserForm = (form) => {
        const data = {
            username: form.username.value,
            password: form.password.value,
            first_name: form.first_name.value,
            last_name: form.last_name.value,
            address: form.address.value,
            city: form.city.value,
            state: form.state.value
        }
        const packet = {
            method: "POST",
            headers: {
                "content-type": "application/json",
                "accept": "application/json"
            },
            body: JSON.stringify(data)
        }

        fetch(usersUrl, packet)
            .then(res => res.json())
            .then(newItem => renderUser(newItem))
            .then(() => form.reset())
    }

    const deleteUser = (e) => {
        const userId = e.parentNode.dataset.id
        const packet = {
            method: "DELETE",
            headers: {
                "content-type": "application/json",
                "accept": "application/json"
            }
        }

        fetch(usersUrl + userId, packet)
            .then(res => res.json())
            .then(() => userContainer.removeChild(e.parentNode))
    }

    const updateUser = (e) => {
        const form = e.parentNode
        const userId = form.dataset.id

        const data = {
            username: form.username.value,
            password: form.password.value,
            first_name: form.first_name.value,
            last_name: form.last_name.value,
            address: form.address.value,
            city: form.city.value,
            state: form.state.value
        }

        const packet = {
            method: "PATCH",
            headers: {
                "content-type": "application/json",
                "accept": "application/json",
            },
            body: JSON.stringify(data)
        }
        fetch(usersUrl + userId, packet)
            .then(res => res.json())
            .then(() => renderUsers())
            .then(() => renderNewUserFormls())
    }

    const renderNewUserForm = (user = defaultUser) => {
        const formContainer = document.getElementById("forms-container")
        formContainer.innerHTML = ''
        const userForm = document.createElement("form")
        userForm.id = "new-user-form"

        userForm.innerHTML = `
            <input name="username" type="text" placeholder="Username" value="${user.username}"><br>
            <input name="password" type="text" placeholder="Password" value="${user.password}"><br>
            <input name="first_name" type="text" placeholder="First-name" value="${user.first_name}"><br>
            <input name="last_name" type="text" placeholder="Last Name" value="${user.last_name}"><br>
            <input name="address" type="text" placeholder="Address" value="${user.address}"><br>
            <input name="city" type="text" placeholder="city" value="${user.city}"><br>
            <input name="state" type="text" placeholder="state" value="${user.state}"><br>
            <input type="submit">
        `
        formContainer.append(userForm)
    }

    const renderUpdateUserForm = (button) => {
        const user = button.parentNode.dataset
        const formContainer = document.getElementById("forms-container")
        formContainer.innerHTML = ''
        const userForm = document.createElement("form")
        userForm.dataset.id = user.id
        userForm.id = "update-user-form"

        userForm.innerHTML = `
            <input name="username" type="text" placeholder="Username" value="${user.username}"><br>
            <input name="password" type="text" placeholder="Password" value="${user.password}"><br>
            <input name="first_name" type="text" placeholder="First-name" value="${user.first_name}"><br>
            <input name="last_name" type="text" placeholder="Last Name" value="${user.last_name}"><br>
            <input name="address" type="text" placeholder="Address" value="${user.address}"><br>
            <input name="city" type="text" placeholder="city" value="${user.city}"><br>
            <input name="state" type="text" placeholder="state" value="${user.state}"><br>
            <button>Update User</button>
        `
        formContainer.append(userForm)
    }

    submitHandler()
    renderUsers()
    clickHandler()
    renderNewUserForm()

})