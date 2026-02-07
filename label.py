def on_click():
    lbl.config(text="button clicked")


lbl = tk.Label(root, text="Hello World")
lbl.grid(column=0, row=0)

print(lbl.config().keys())

btn=tk.Button(root, text="Click Me", command=on_click).grid(column=1, row=1)

root.mainloop()