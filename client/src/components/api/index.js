import Vue from 'vue';

// The EventBus variable is an instance of the Vue object.
//  Vue object has both an $emit and a pair of $on / $off methods,
//  which are used to emit events as well as register and unregister to events.
export const EventBus = new Vue();

