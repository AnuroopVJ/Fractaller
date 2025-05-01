import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import BOTH, Canvas, Tk

from fractal_func import mandelbrot, juila_set, generate_buddhabrot,make_non_mandelbrot_set

def cmap_func(choice):
    if choice == "Select an option":
        print("Please select an option")
        return None
    return choice

def generate_j_fractal(range_input, max_iterations, linear_resolution, cmap_ch, center_input, power_input):
    try:
        cmap_ch = dropdown.get()
        max_iterations = int(max_iterations.get())  # Convert to integer
        linear_resolution = float(linear_resolution.get())  # Convert to float
        center_input = complex(center_input.get())  # Convert to complex
        range_input = range_input.get()
        power_input = int(power_input.get())  # Convert to integer
        if range_input == "None":
            range_input = None
        else:
            range_input = float(range_input)

        juila_set(range_input, max_iterations, linear_resolution, cmap_ch, center_input, power=power_input)
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(e)

def generate_m_fractal():
    try:
        cmap_ch = dropdown.get()
        n_rows = get_n_rows(n_rows_inp)
        n_columns = get_n_columns(n_columns_inp)
        
        if cmap_ch and n_rows and n_columns:
            mandelbrot(n_rows, n_columns, 50, cmap_ch)
        else:
            print("Please ensure all inputs are valid.")
    except Exception as e:
        print(e)

def generate_b_fractal(size_input, nsamples_input, max_iterations_input):
    try:
        cmap_ch = dropdown.get()
        size = int(size_input.get())  # Convert to integer
        nsamples = int(nsamples_input.get())  # Convert to integer
        max_iterations = int(max_iterations_input.get())  # Convert to integer

        if cmap_ch and size and nsamples and max_iterations:
            generate_buddhabrot(make_non_mandelbrot_set(nsamples, max_iterations), size)
        else:
            print("Please ensure all inputs are valid.")
    except Exception as e:
        print(e)

def get_n_rows(entry):
    try:
        value = entry.get()
        if value:
            return int(value)
        else:
            print("Please enter a valid number for n_rows")
            return None
    except ValueError as e:
        print(f"Invalid input for n_rows: {e}")
        return None

def get_n_columns(entry):
    try:
        value = entry.get()
        if value:
            return int(value)
        else:
            print("Please enter a valid number for n_columns")
            return None
    except ValueError as e:
        print(f"Invalid input for n_columns: {e}")
        return None

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("1000x450")
app.title("Fractaller")
app.iconbitmap(r"C:\Users\neela\Desktop\Miscellaneous\coding\Fractal_app\org_94177.ico")

# Color map selection
cmap_label = ctk.CTkLabel(app, text="Color Map:", fg_color="transparent")
cmap_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

cmaps = ["Accent", "Blues", "Greens", "Oranges", "Reds", "viridis", "plasma", "inferno", "magma", "cividis"]
dropdown = ctk.CTkOptionMenu(master=app, values=cmaps, command=cmap_func)
dropdown.set("Select an option:")
dropdown.grid(row=0, column=1, padx=20, pady=(20, 5), sticky="ew")

# Mandelbrot Section
mandelbrot_frame = ctk.CTkFrame(app)
mandelbrot_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

mandelbrot_label = ctk.CTkLabel(mandelbrot_frame, text="Mandelbrot Set", font=("Arial", 16, "bold"))
mandelbrot_label.grid(row=0, column=0, columnspan=2, pady=10)

x_axis_label = ctk.CTkLabel(mandelbrot_frame, text="X-axis resolution:")
x_axis_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
n_rows_inp = ctk.CTkEntry(mandelbrot_frame, placeholder_text="Enter resolution")
n_rows_inp.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

y_axis_label = ctk.CTkLabel(mandelbrot_frame, text="Y-axis resolution:")
y_axis_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
n_columns_inp = ctk.CTkEntry(mandelbrot_frame, placeholder_text="Enter resolution")
n_columns_inp.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

mandelbrot_button = ctk.CTkButton(mandelbrot_frame, text="Generate Mandelbrot", command=generate_m_fractal)
mandelbrot_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

# Julia Set Section
julia_frame = ctk.CTkFrame(app)
julia_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

julia_label = ctk.CTkLabel(julia_frame, text="Julia Set", font=("Arial", 16, "bold"))
julia_label.grid(row=0, column=0, columnspan=2, pady=10)

iterations_label = ctk.CTkLabel(julia_frame, text="Max iterations:")
iterations_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
max_iterations = ctk.CTkEntry(julia_frame, placeholder_text="Enter max iterations")
max_iterations.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

resolution_label = ctk.CTkLabel(julia_frame, text="Linear resolution:")
resolution_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
linear_resolution = ctk.CTkEntry(julia_frame, placeholder_text="Enter resolution")
linear_resolution.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

center_label = ctk.CTkLabel(julia_frame, text="Center (e.g., -0.05-0.66j):")
center_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
center_input = ctk.CTkEntry(julia_frame, placeholder_text="Enter center")
center_input.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

power_label = ctk.CTkLabel(julia_frame, text="Power:")
power_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
power_input = ctk.CTkEntry(julia_frame, placeholder_text="Enter power")
power_input.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

range_label = ctk.CTkLabel(julia_frame, text="Range (e.g., None or 2.0):")
range_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
range_input = ctk.CTkEntry(julia_frame, placeholder_text="Enter range")
range_input.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

julia_button = ctk.CTkButton(julia_frame, text="Generate Julia", command=lambda: generate_j_fractal(range_input, max_iterations, linear_resolution, dropdown.get(), center_input, power_input))
julia_button.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

# Buddhabrot Section
buddhabrot_frame = ctk.CTkFrame(app)
buddhabrot_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

buddhabrot_label = ctk.CTkLabel(buddhabrot_frame, text="Buddhabrot", font=("Arial", 16, "bold"))
buddhabrot_label.grid(row=0, column=0, columnspan=2, pady=10)

size_label = ctk.CTkLabel(buddhabrot_frame, text="Image size:")
size_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
size_input = ctk.CTkEntry(buddhabrot_frame, placeholder_text="Enter size")
size_input.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

nsamples_label = ctk.CTkLabel(buddhabrot_frame, text="Number of samples:")
nsamples_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
nsamples_input = ctk.CTkEntry(buddhabrot_frame, placeholder_text="Enter samples")
nsamples_input.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

max_iterations_label = ctk.CTkLabel(buddhabrot_frame, text="Max iterations:")
max_iterations_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
max_iterations_input = ctk.CTkEntry(buddhabrot_frame, placeholder_text="Enter max iterations")
max_iterations_input.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

buddhabrot_button = ctk.CTkButton(buddhabrot_frame, text="Generate Buddhabrot", command=lambda: generate_b_fractal(size_input, nsamples_input, max_iterations_input))
buddhabrot_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

app.mainloop()
