import os
import json

#################
### CONSTANTS ###
#################

IMAGE_HEIGHT = 32
IMAGE_WIDTH = 32
IMAGE_CHANNELS = 3

CIFAR_10_PATH = "C:\\Users\\zbamberg\\PycharmProjects\\CNN\\CNN\\cifar\\cifar-10-batches-py"
CIFAR_100_PATH = "C:\\Users\\zbamberg\\PycharmProjects\\CNN\\CNN\\cifar\\cifar-100-python"


class Batch:
    COUNTER = 0

    def __init__(self, batch_dict):
        self.images = self.make_images(batch_dict['data'.encode()])
        self.tags = batch_dict['labels'.encode()]
        self.name = "CIFAR-10-BATCH-" + str(Batch.COUNTER)
        self.number = Batch.COUNTER
        print("Done initializing batch: " + self.name)
        Batch.COUNTER += 1

    @staticmethod
    def make_images(data):
        """

        :param data: An array of N images. Each image is 32x32 pixels.
        Each row in data represents an image. For each row in the image,
        we represent first the 32 RED values, then the 32 GREEN values,
        and finally, the 32 BLUE values. This pattern appears 32 times --
        in accordance with the number of "columns" in a particular row.
        :return: An array of N 32x32x3 images.
        """
        images = []
        for image in range(len(data)):
            print("Processing image number " + str(image))
            source_image = data[image]
            current_image = []
            for row in range(IMAGE_HEIGHT):
                current_row = []
                for column in range(IMAGE_WIDTH):
                    current_entry = []
                    for channel in range(IMAGE_CHANNELS):
                        ind = row * column * IMAGE_CHANNELS + channel
                        current_entry.append(int(source_image[ind]))
                    current_row.append(current_entry)
                current_image.append(current_row)
            images.append(current_image)
        print("All done!")
        return images

    def write_to_json(self):
        """

        :param name: The name of the json file we are going to write
        :return: None
        """

        ORIGINAL_PATH = os.getcwd()

        print("Writing " + self.name + " to JSON")
        if not os.path.isdir("images"):
            os.mkdir("images")
        os.chdir("images")

        image_dict = {}
        for image_num in range(len(self.images)):
            image_dict[image_num] = self.images[image_num]
            file_name = self.name + "-IMAGE-" + str(image_num) + ".txt"
            print("Writing image #" + str(image_num))
            with open(file_name, 'w') as fileHandle:
                fileHandle.write(json.dumps(image_dict))


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        my_dict = pickle.load(fo, encoding='bytes')
    return my_dict


if __name__ == "__main__":
    os.chdir(CIFAR_10_PATH)
    dicts = []
    for x in range(5):
        num = str(x + 1)
        name = "data_batch_" + num
        dicts.append(unpickle(name))

    batches = []
    for d in dicts:
        print("Starting to process bath " + str(d["batch_label".encode()]))
        batch = Batch(d)
        batches.append(batch)
