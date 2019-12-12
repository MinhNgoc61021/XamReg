<template>
    <div class="container">
        <h1 class="title is-3">Đăng ký thi</h1>
        <h2 class="subtitle is-6">Sinh viên đăng ký ca thi mà sinh viên đủ điều kiện dự thi và đang còn chỗ trống</h2>
        <b-collapse
            class="card"
            v-for="(collapse, index) of collapses"
            :key="index"
            :open="isOpen === index"
            @open="isOpen = index">
            <div
                slot="trigger"
                slot-scope="props"
                class="card-header"
                role="button">
                <p class="card-header-title">
                    {{ collapse.title }}
                </p>
                <a class="card-header-icon">
                    <b-icon
                        :icon="props.open ? 'menu-down' : 'menu-up'">
                    </b-icon>
                </a>
            </div>
            <div class="card-content">
                <div class="content">
                    {{ collapse.text }}
                </div>
            </div>
        </b-collapse>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                isOpen: 0,
                collapses: [
                {
                    title: 'Title 1',
                    text: 'Text 1'
                },
                {
                    title: 'Title 2',
                    text: 'Text 2'
                },
                {
                    title: 'Title 3',
                    text: 'Text 3'
                }
                ]
            }
        }
    }
</script>
