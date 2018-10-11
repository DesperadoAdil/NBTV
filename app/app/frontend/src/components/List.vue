<template>
	<div id="list">
		<ul>
			<li v-for="item in items">
				<Card class="card">
					<router-link to="/living"><img class="thumbnail" :src='item.thumbnail'></router-link>
					<div class="classroomDetail" style="text-align:center">
						<span class="title">
							{{ item.title }}
						</span>
						<span class="teacher">
							{{ item.teacher }}
						</span>
						<span class="id">
							{{ item.id }}
						</span>
					</div>
				</Card>
			</li>
		</ul>
	</div>

</template>
<script>
	import axios from 'axios';
	export default {
	  name: 'List',
	  data () {
	    return {
				items: [
					{
						id: '',
						teacher: '',
						title: '',
						thumbnail: '',
						password: '',
						url: '',
						studentlist: '',
						teacherlist: '',
						audiencelist: '',
						visible: ''
					},
				]
	    }
	  },
		created() {
			this.getList();
		},
		methods: {
			getList() {
				axios.get('/api/list').then((resp) => {
					console.log(resp)
					this.items = resp.data;
				})
			}
		}

	}
</script>
<style>
	ul {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
	}
	li {
		list-style: none;
	}
	.card {
		width: 320px;
		height: 200px;
	}
	.previewPicture {
		width: 288px;
		height: 120px;
	}
</style>
