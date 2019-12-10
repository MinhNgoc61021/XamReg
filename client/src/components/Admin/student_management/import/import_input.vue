<template>
    <b-tabs type="is-toggle" expanded >
        <b-tab-item label="Nhập bằng Excel" icon-pack="fas" icon="file-excel" style="margin: auto">
            <component v-bind:is="upload"/>
        </b-tab-item>
        <b-tab-item label="Nhập bằng form" icon-pack="fas" icon="keyboard">
            <component v-bind:is="form"/>
        </b-tab-item>
    </b-tabs>
</template>
<script>
    import upload from './upload/upload';
    import form from './form/form';

    export default {
        name: "import",
        components: {
          upload, form
        },
        data() {
            return {
              upload, form
            }
        }
    }
</script>

<style scoped>

</style>
