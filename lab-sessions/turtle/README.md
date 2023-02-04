# Start Up instructions

To run this example, simply run the command below:

```
python app.py --host <docker-container-ip-address> --port 8030
```

Where the `<docker-container-ip-address>` is to be found from the `ifconfig` command, looking at the first network interface that shows up, from within the container itself.

Then, open the browser and go to the URL: `http://<docker-container-ip-address>:8030`
Edit the `turtle_graphics.py` script
Refresh the above webpage to see the effects of your edits.


