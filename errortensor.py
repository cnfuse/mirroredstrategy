import tensorflow as tf

# Example tensor creation on CPU
cpu_tensor = tf.constant([1, 2, 3, 4, 5], dtype=tf.float32)

# Ensure tensor is initialized properly
if cpu_tensor is not None:
    try:
        # Attempt to transfer the tensor to GPU
        gpu_tensor = cpu_tensor.gpu()
        print("Tensor transferred to GPU successfully.")
    except tf.errors.InternalError as e:
        print(f"Error transferring tensor to GPU: {e}")
else:
    print("Tensor is not initialized.")

