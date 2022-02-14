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
              <v-dialog
                transition="dialog-bottom-transition"
                max-width="600"
              >
                <template v-slot:activator="{ on, attrs }">
                  <a color="primary" v-bind="attrs" v-on="on">Don't see your University?</a>
                </template>
                <template v-slot:default="dialog">
                  <v-card>
                    <v-card-title>
                      Adding a University to ChatFinder.
                    </v-card-title>
                    <v-card-text>
                      Since I don't want to clutter this list, Universities are added by me personally.
                      
                      To add your university to ChatFinder, please send an Issue here.
                    </v-card-text>
                    <v-card-actions class="justify-end">
                      <v-btn
                        text
                        @click="dialog.value = false"
                      >Close</v-btn>
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
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
              <v-dialog
                transition="dialog-bottom-transition"
                max-width="600"
                v-model="unit_dialog"
              >
                <template v-slot:activator="{ on, attrs }">
                  <a color="primary" v-bind="attrs" v-on="on">Don't see your Unit/Course</a>
                </template>
                <template v-slot:default="dialog">
                  <v-form v-model="chat_code_valid"> 
                  <v-card>
                    <v-card-title>
                      Add a Unit/Course.
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12" md="12">
                              <v-text-field
                                v-model="chat_code_name"
                                :rules="chat_code_name_rules"
                                label="Unit/Course Name?"
                                required
                              >
                              </v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions class="justify-end">
                      <v-btn
                        text
                        @click="createUnitCode"
                        :disabled="!chat_code_valid"
                      >Create</v-btn>
                      <v-btn
                        text
                        @click="dialog.value = false"
                      >Close</v-btn>
                    </v-card-actions>
                  </v-card>
                  </v-form>
                </template>
              </v-dialog>
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
                      {{ chat.group_type == 'discord' ? 'mdi-discord' : (chat.group_type == "facebook" ? 'mdi-facebook' : 'mdi-help-circle') }}
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

    unit_dialog: false,

    chat_code_valid: false,
    chat_code_name: "",
    chat_code_name_rules: [
      v => !!v || 'A unit/course name is required',
    ]
  }),
  
  methods: {
    updateUniversityList: function() {
      this.total_loading = true;
      axios.get('http://127.0.0.1:8000/api/universities/')
        .then( response => {
          this.uni_options = response.data;
          this.total_loading = false;
        })
    },
    updateChatCodeList: function() {
      this.uni_loading = true;
      axios.get(`http://127.0.0.1:8000/api/chat_codes/${this.university}/`)
        .then(response => {
          this.chat_code_options = response.data;
          this.uni_loading = false;
        })
    },
    updateChatList: function() {
      this.chat_code_loading = true;
      axios.get(`http://127.0.0.1:8000/api/chats/${this.chat_code}/`)
        .then(response => {
          this.chats = response.data;
          this.chat_code_loading = false;
        })
    },
    createUnitCode: function() {
      axios.post(`http://127.0.0.1:8000/api/chat_codes/${this.university}/`, {
        "show_name": this.chat_code_name,
        "university": this.university
      }).then(() => {
        this.updateChatCodeList();
        this.unit_dialog = false;
      }).catch(err => {
        // TODO: Actually show errors.
        console.log(err);
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
        this.updateChatCodeList();
      } else {
        this.chat_code_options = [];
      }
    },
    chat_code(newChat) {
      if (newChat != "" && newChat != null) {
        this.updateChatList();
      } else {
        this.chats = [];
      }
    }
  }  
};
</script>
