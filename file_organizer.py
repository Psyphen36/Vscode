import shutil


def organize_file(source_dir, destination_dir):
	files = os.listdir(source_dir)

	for file in files:
		file_path = os.path.join(source_dir, file)

		if os.path.isfile(file_path):
			_, extension = os.path.splitext(file)

			destination_folder = os.path.join(destination_dir, extension[1:].lower())
			os.makedirs(destination_folder, exist_ok=True)

			shutil.move(file_path, destination_folder)

	print('File organization completed successfully!!')


clutter_dir = '/home/anupam/PycharmProjects/pythonProject2'
organized_dir = '/home/anupam/PycharmProjects/pythonProject2/Organized_files'

organize_file(clutter_dir, organized_dir)
