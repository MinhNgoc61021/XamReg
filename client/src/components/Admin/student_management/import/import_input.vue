<template>
    <b-tabs type="is-toggle" expanded >
        <b-tab-item label="Nhập bằng Excel" icon-pack="fas" icon="file-excel" c style="margin: auto">
          <keep-alive>
            <component v-bind:is="upload"/>
          </keep-alive>

        </b-tab-item>
        <b-tab-item label="Nhập bằng form" icon-pack="fas" icon="keyboard">
          <keep-alive>
            <component v-bind:is="input"/>
          </keep-alive>
        </b-tab-item>
    </b-tabs>
</template>
<script>
    import upload from './upload/upload';
    import input from './input/input';

    export default {
        name: "import",
        components: {
          upload, input
        },
        data() {
            return {
              upload, input
            }
        }
    }
</script>

<style scoped>

</style>
