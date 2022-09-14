<script setup>
import { ref } from 'vue';
const APIexample = ref([
    {'key': 'API Key 1', 'channel': 'LINE Ch 1', 'reminderlist': [
        {
            'schedule': '2022/9/15',
            'content': 'あれをやる'
        },
        {
            'schedule': '2022/9/22',
            'content': 'あれをやる'
        }
        ],
        'show': false
    },
    {'key': 'API Key 2', 'channel': 'LINE Ch 2', 'reminderlist': [
        {
            'schedule': '2022/9/15',
            'content': 'それをやる'
        },
        {
            'schedule': '2022/9/22',
            'content': 'どれをやる'
        }
        ],
        'show': false
    }
]);

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
            <v-container>
            <v-row justify="center"><v-col cols="8">
                <h2>API List</h2>
                <div v-for="(APIkey, index) in APIexample" :key="index">
                    <v-card elevation="3" class="mx-auto my-2">
                        <v-card-title> {{ APIkey.channel }} </v-card-title>
                        <v-card-text> {{ APIkey.key }} </v-card-text>
                    <v-card-actions>
                        <v-btn color="#4CC764" text>
                            Remind list
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn icon @click="APIkey.show = !APIkey.show">
                            <v-icon>{{ APIkey.show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                        </v-btn>
                    </v-card-actions>
                    <v-expand-transition>
                        <div v-show="APIkey.show">
                            <v-divider></v-divider>
                            <v-card-text v-for="(APIcontent, indexC) in APIkey.reminderlist" :key="indexC">
                            {{ APIcontent.schedule }}: {{ APIcontent.content }}
                            </v-card-text>
                        </div>
                    </v-expand-transition>
                </v-card>
                </div>
            </v-col></v-row>
            </v-container>
        </div>
    </div>
    </v-app>
</template>
