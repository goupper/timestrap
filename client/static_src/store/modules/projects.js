import Vue from 'vue';

import fetch from '../../fetch';


export default {
  namespaced: true,
  state: {
    all: [],
  },
  getters: {
    getNumberOfProjects: state => {
      return state.all.length;
    },
    getSelectProjects: state => {
      return state.all.map(project => {
        return {id: project.url, text: project.name};
      });
    },
    getSearchProjects: state => search => {
      return state.all.filter(project => {
        return project.name.toLowerCase().includes(search) || project.client_details.name.toLowerCase().includes(search);
      });
    },
  },
  mutations: {
    setProjects: (state, projects) => state.all = projects,
    addProject: (state, project) => state.all.unshift(project),
    updateProject: (state, opts) => Vue.set(state.all, opts.index, opts.project),
    removeProject: (state, index) => Vue.delete(state.all, index),
  },
  actions: {
    getProjects({commit}) {
      commit('addLoading', 'projects', {root: true});
      fetch.get(timestrapConfig.API_URLS.PROJECTS).then(response => {
        commit('setProjects', response.data);
        commit('removeLoading', 'projects', {root: true});
      }).catch(error => console.log(error));
    },
    createProject({commit}, project) {
      fetch.post(timestrapConfig.API_URLS.PROJECTS, project).then(response => {
        commit('addProject', response.data);
      }).catch(error => console.log(error));
    },
    editProject({commit, state}, project) {
      fetch.put(project.url, project).then(response => {
        const index = state.all.findIndex(item => {
          return item.id === response.data.id;
        });
        commit('updateProject', {index: index, project: response.data});
      }).catch(error => console.log(error));
    },
    deleteProject({commit, state}, project) {
      const index = state.all.findIndex(item => {
        return item.id === project.id;
      });
      fetch.delete(state.all[index].url).then(() => {
        commit('removeProject', index);
      }).catch(error => console.log(error));
    },
  },
};
