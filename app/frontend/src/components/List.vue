<template>
	<div id="list">
		<ul>
			<li v-for="item in items">
				<Card class="card">
					<img class="previewPicture" :src='item.image'>
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
						image: '这里应该是一个图片的url'
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
					this.items = resp;
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
