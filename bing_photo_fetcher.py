import argparse
from bing_image_downloader import downloader

class ImageDownloader:
    def __init__(self, search_queries=["Football", "soccer"], num_images_per_query= 100, output_folder_name="images"):
        self.search_queries = search_queries
        self.num_images_per_query = num_images_per_query
        self.output_folder_name = output_folder_name

    def download_images(self):
        for query in self.search_queries:
            downloader.download(query, limit=self.num_images_per_query, output_dir=self.output_folder_name, force_replace=False, timeout=60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images using Bing Image Downloader.")
    parser.add_argument("--search_queries", nargs="+", default=["Football", "soccer"], help="List of search queries to download images for.")
    parser.add_argument("--num_images_per_query", type=int, default=100, help="Number of images to download for each query.")
    parser.add_argument("--output_folder_name", default="images", help="Folder to save downloaded images.")

    args = parser.parse_args()

    img_downloader = ImageDownloader(args.search_queries, args.num_images_per_query, args.output_folder_name)
    img_downloader.download_images()

