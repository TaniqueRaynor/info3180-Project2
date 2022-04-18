<script>
export default {
    created(){
        this.getCsrfToken();
    },
    data(){
        return {
            csrf_token: ''
        }
    },
    methods : {
        login(){

            let loginForm = document.getElementById('loginForm');
            let form_data = new FormData(loginForm);

            fetch("/api/auth/login", {
                method: 'POST',
                body: form_data,
                headers: {'X-CSRFToken': this.csrf_token}
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                
                if (data.status == 200){
                    
                }
                
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        }
    },
}
</script>

<template>

    <div id="status" hidden>

    </div>

    <form @submit.prevent="login" id="loginForm" method="POST">

        <div class="form-group">
            <label for="description">Description: </label>
            <textarea class="form-control rounded-0" id="" rows="10" name="description"></textarea>

        </div>

        <div class="form-group">
            <label class="form-label" for="photo">Photo Upload</label>
            <input class="form-control" type="file" name="photo" id="">
        </div>

        <button class="btn btn-primary" type="submit" style="margin-top: 10px; margin-bottom: 10px;">Submit</button>

    </form>
    
</template>

<style>

</style>