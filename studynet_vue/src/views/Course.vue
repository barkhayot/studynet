
   
<template>
    <div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">{{course.title}}</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h2>Table of contents</h2>

                        <ul>
                            <li>
                                <a >hey</a>
                            </li>
                            <li>
                                <a >hey2</a>
                            </li>
                        </ul>
                    </div>

                    <div class="column is-10">
                        <template v-if="$store.state.user.isAuthenticated">
                                <h2>Introduciton</h2>
                                
                               <p> {{course.long_description}}</p>
                        </template>

                        <template v-else>
                            <h2>Restricted access</h2>
                            
                            <p>You need to have an account to continue!</p>
                        </template>
                                <hr>

                                <article 
                                    class="media box"
                                    
                                >
                                    <div class="media-content">
                                        <div class="content">
                                            <p>
                                                comment
                                            </p>
                                        </div>
                                    </div>
                                </article>

                                <form >
                                    <div class="field">
                                        <label class="label">Name</label>
                                        <div class="control">
                                            <input type="text" class="input">
                                        </div>
                                    </div>

                                    <div class="field">
                                        <label class="label">Content</label>
                                        <div class="control">
                                            <textarea class="textarea"></textarea>
                                        </div>
                                    </div>

                                    <div 
                                        class="notification is-danger"
                            
                                    >
                                        {{ error }}
                                    </div>

                                    <div class="field">
                                        <div class="control">
                                            <button class="button is-link">Submit</button>
                                        </div>
                                    </div>
                                </form>
                            
                                Description
                            
                            <h2>Restricted access</h2>
                            
                            <p>You need to have an account to continue!</p>
                        
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            course: []
        }
    },
    
    mounted() {
        console.log('mounted')

        const slug = this.$route.params.slug

        axios
            .get(`/api/v1/courses/${slug}/`)
            .then(response => {
                console.log(response.data)
                this.course = response.data
            })
    }
}
</script>