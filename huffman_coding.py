# Description: This module contains the functions to calculate the entropy and average Huffman code length

import cv2
import numpy as np
from collections import Counter
import heapq
import grayscale

def calculate_entropy(image):
    """
    Calculate the entropy of an image.
    Parameters: image (numpy.ndarray): The input image.
    Returns: The entropy of the image.
    
    """
    _, counts = np.unique(image, return_counts=True)
    probabilities = counts / np.sum(counts)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def huffman_tree(frequencies):
    """Construct the Huffman tree based on frequencies.
    
    Parameters: frequencies (dict): A dictionary of symbol frequencies.
    
    Returns: A list of tuples representing the Huffman tree nodes.
    """
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def huffman_main(image_path):
    """
    Main function to calculate the 
    entropy and average Huffman code length
    of an image.

    Parameters:image_path (str): Path to the image file.

    Returns: A list containing the entropy and average Huffman code length.
    """

    image = grayscale.grayscale(image_path, 'gray_image.bmp')
    cv2.imwrite('output_images/huffman_image.bmp', image)
    # Calculate the entropy of the image
    image_entropy = calculate_entropy(image)
    print(f"Entropy of the image: {image_entropy:.2f} bits")
    # Calculate the average Huffman code length
    frequencies = dict(Counter(image.flatten()))
    huffman_tree_nodes = huffman_tree(frequencies)
    code_lengths = {item[0]: len(item[1]) for item in huffman_tree_nodes}
    total_pixels = image.size
    avg_code_length = sum(length * frequencies[symbol] for symbol, length in code_lengths.items()) / total_pixels
    print(f"Average Huffman code length: {avg_code_length:.2f} bits")
    return [image_entropy, avg_code_length]


