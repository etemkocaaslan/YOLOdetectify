from bing_image_downloader import downloader

class ImageDownloader:
    def __init__(self, search_queries, num_images_per_query, output_folder_name):
        self.search_queries = search_queries
        self.num_images_per_query = num_images_per_query
        self.output_folder_name = output_folder_name

    def download_images(self):
    	for query in self.search_queries:
        	downloader.download(query, limit=self.num_images_per_query, output_dir=self.output_folder_name, force_replace=False, timeout=60)


if __name__ == "__main__":
    search_queries = ["Football, soccer"]
    num_images_per_query = 100
    output_folder_name = 'images'

    img_downloader = ImageDownloader(search_queries, num_images_per_query, output_folder_name)
    img_downloader.download_images()

