<script setup>
    import { ref } from 'vue';
</script>

<template>
    <v-app id="app">
    <div id="parent">
        <v-app-bar color="#4CC764" dark>
        <div id="header">
            <h1>LINE API Manager</h1>
        </div>
        </v-app-bar>
        <div id="field">
            <v-row justify="center"><v-col cols="8">
                    <h2>API List</h2>
                    <v-card elevation="3">
                    API Key 1
                    </v-card>
            </v-col></v-row>
            
        </div>
    </div>
    </v-app>
</template>
