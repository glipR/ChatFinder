<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <h2>ChatFinder</h2>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <v-row class="text-center">

          <v-col cols="12" id="uni_pick" v-show="total_loading">
            <v-progress-circular
              indeterminate
              color="red"
            ></v-progress-circular>
          </v-col>

          <v-col cols="12" id="uni_pick" v-show="!total_loading">
            <h3>Select University</h3>
            <div style="max-width: 600px; margin: auto">
              <v-autocomplete
                v-model="university"
                :items="uni_options"
                item-text="show_name"
                item-value="id"
                prepend-icon="mdi-city"
              ></v-autocomplete>
            </div>
          </v-col>

          <v-col cols="12" id="uni_pick" v-show="university != '' && !uni_loading">
            <h3>Select Unit/Course</h3>
            <div style="max-width: 600px; margin: auto">
              <v-autocomplete
                v-model="chat_code"
                :items="chat_code_options"
                item-text="show_name"
                item-value="id"
                prepend-icon="mdi-city"
              ></v-autocomplete>
            </div>
          </v-col>
          <v-col cols="12" id="uni_pick" v-show="university != '' && uni_loading">
            <v-progress-circular
              indeterminate
              color="red"
            ></v-progress-circular>
          </v-col>

          <v-col cols="12" id="uni_pick" v-show="chat_code != '' && !chat_code_loading">
            <h3>Join Chats!</h3>
            <div style="max-width: 600px; margin: auto">
              <v-list
                subheader
                two-line
              >
                <v-subheader inset>Chats</v-subheader>
                <v-list-item
                  v-for="chat in chats"
                  :key="chat.id"
                >
                  <v-list-item-avatar>
                    <v-icon
                      class="grey lighten=1"
                      dark
                    >
                      {{ chat.group_type == 'discord' ? 'mdi-discord' : (chat.group_type == "facebook" ? 'mdi-facebook' : 'mdi-question') }}
                    </v-icon>
                  </v-list-item-avatar>
                  <v-list-item-content style="text-align: left">
                    <v-list-item-title v-text="chat.show_name"></v-list-item-title>
                    <v-list-item-subtitle v-text="`${chat.year}`"></v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-avatar>
                    <v-icon
                      color="green"
                    >
                      mdi-plus
                    </v-icon>
                  </v-list-item-avatar>
                  <v-list-item-content style="text-align: left">
                    <v-list-item-title>Add new chat</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </div>
          </v-col>
          <v-col cols="12" id="uni_pick" v-show="chat_code != '' && chat_code_loading">
            <v-progress-circular
              indeterminate
              color="red"
            ></v-progress-circular>
          </v-col>

        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',

  components: {
    // HelloWorld,
  },

  data: () => ({
    total_loading: true,
    uni_loading: false,
    chat_code_loading: false,
    university: "",
    chat_code: "",
    uni_options: [],
    chat_code_options: [],
    chats: [],
  }),
  
  methods: {
    updateUniversityList: function() {
      axios.get('http://127.0.0.1:8000/api/universities/')
        .then( response => {
          this.uni_options = response.data;
          this.total_loading = false;
        })
    }
  },

  created() {
    this.updateUniversityList();
  },

  watch: {
    university(newUni) {
      this.chat_code = "";
      if (newUni != "" && newUni != null) {
        this.uni_loading = true;
        axios.get(`http://127.0.0.1:8000/api/chat_codes/${newUni}/`)
          .then(response => {
            this.chat_code_options = response.data;
            this.uni_loading = false;
          })
      } else {
        this.chat_code_options = [];
      }
    },
    chat_code(newChat) {
      if (newChat != "" && newChat != null) {
        this.chat_code_loading = true;
        axios.get(`http://127.0.0.1:8000/api/chats/${newChat}/`)
          .then(response => {
            this.chats = response.data;
            this.chat_code_loading = false;
          })
      } else {
        this.chats = [];
      }
    }
  }  
};
</script>
