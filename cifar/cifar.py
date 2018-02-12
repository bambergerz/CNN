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
        """

        :param batch_dict: A dictionary obtained by unpickling batch files from either cifar-10 or cifar-100.
        """
        Batch.COUNTER += 1
        self.images = self.make_images(batch_dict['data'.encode()])
        self.tags = batch_dict['labels'.encode()]
        self.name = "CIFAR-10-BATCH-" + str(Batch.COUNTER)
        self.number = Batch.COUNTER
        print("Done initializing batch: " + self.name)

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
            # print("Processing image number " + str(image))
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
        # print("All done!")
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

        os.chdir(ORIGINAL_PATH)


def unpickle(file):
    """

    :param file: the name of a batch file to unpickle
    :return: A dictionary representing the batch.
    Can be turned into a Batch object via feeding this dict into the Batch constructor.
    """
    import pickle
    with open(file, 'rb') as fo:
        my_dict = pickle.load(fo, encoding='bytes')
    return my_dict


def get_batch(num):
    """

    :param num: The number of the batch we would like to process. An int between 1 and 5
    :return: the batch object representing the desired batch.
    """
    assert isinstance(num, int)
    assert 0 < num < 6
    current_loc = os.getcwd()
    os.chdir(CIFAR_10_PATH)
    batch_dict = unpickle("data_batch_" + str(num + 1))
    batch = Batch(batch_dict)
    os.chdir(current_loc)
    return batch
