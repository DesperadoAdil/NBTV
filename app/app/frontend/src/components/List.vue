<template>
	<div id="list">
		<ul>
			<li v-for="item in items">
				<Card class="card">
					<router-link to="/living"><img class="previewPicture" :src='item.image'></router-link>
					<div class="classroomDetail" style="text-align:center">
						<span class="className">
							{{ item.className }}
						</span>
						<span class="teacherName">
							{{ item.teacherName }}
						</span>
						<span class="viewingNumber">
							{{ item.viewing }}
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
						className: '第一课',
						teacherName: '习近平',
						viewing: '100亿人正在观看',
						image: '这里应该是一个图片的url',
						id: ''
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
