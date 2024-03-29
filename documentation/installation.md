# Installing and setting up YERP!

First things first: this is not yet a tried and tested solution. Installations of YERP! should be done at this point for testing and development. And any testing out in the world should be done alongside already functioning emergency/bathroom protocols to address overdose/medical emergencies.

Second  things second: simplifying this installation process is a primary concern for this project! Much of this process, certainly everything that comes after the steps for setting up Home Assistant and HACS, can hypothetically become far more simplified given the right code (sadly beyond this current developer's current skill set, though I'll learn as I can! If you'd like to support the project, either sponsoring funding for some outside help here or contributing this as a programmer yourself would be especially helpful!). 

Some working knowledge of [Home Assistant](https://home-assistant.io) and its lexicon will definitely be helpful. If you're not up on such things, [Youtube tutorials](https://www.youtube.com/watch?v=sVqyDtEjudk), [Home Assistant's documentation](https://www.home-assistant.io/docs/) are great places to check out. The [community support forum](https://community.home-assistant.io/) is also a great place to reference if you get stuck.

**Some terms used throughout:**

- **YERP! Installation:** A device running Home Assistant, configured to be used for YERP!
- **YERP! Instance:** A set of sensors and code dedicated to one specific instance of YERP!, such as a single bathroom.
- Additional terms can be found over in the [Home Assistant glossary](https://www.home-assistant.io/docs/glossary/).

### System requirements
- Running installation of [Home Assistant](https://home-assistant.io)
- Motion sensor, preferably one with a short buffer time*
- Door sensor
- Z-Wave/Zigbee radio (dependent on the devices being used; so far we've used HUSBZB-1's as they have both)

#### Optional components
- Siren
- Speaker
- Smart button
- Smart RGBW Bulb
- Tablet or smartphone with Home Assistant app installed

*Most smart-enabled motion sensors deactivate for a given amount of time after sensing  motion to conserve battery life. This commonly ranges from 30 seconds to 2-5 minutes. We've been using Ecolink PIRZWAVE-2.5 sensors, because they have a built in dipswitch for a "testing mode". In some iterations of the sensor that means 5 seconds and in others 7, but either way it's short enough for our purposes. Other options include a hack for Xiaomi Aqara PIR sensors to enable a 5 second buffer (hasn't been tested with YERP! yet but sounds pretty nice!), and DIY sensors built with ESP boards like the Wemos D1 Mini and HC-SR501 sensors (which run around $5 in parts, would need some sort of enclosure, and can run on ESPHome or Tasmota)

### Installing and setting up Home Assistant

1. See [Home Assistant's documentation](https://www.home-assistant.io/installation/) on how to get an installation up and running. 
2. There are a few Home Assistant addons you'll probably want to get going, to make the rest of this process and ongoing use/development/maintenance a lot easier. We use:

- [Studio Code Server](https://github.com/hassio-addons/addon-vscode)
- [Terminal/SSH](https://github.com/hassio-addons/addon-ssh)
- [Portainer](https://github.com/hassio-addons/addon-portainer)
- [MariaDB](https://github.com/home-assistant/hassio-addons/tree/master/mariadb)
- [Zwave.js](https://github.com/home-assistant/hassio-addons/tree/master/zwave_js), which would only be necessary if you're using Z-Wave devices.
- [Mosquitto](https://github.com/home-assistant/hassio-addons/tree/master/mosquitto), only necessary if you're using MQTT-enabled devices.
- [Hass.io Access Point](https://github.com/mattlongman/hassio-access-point), if you'd like to use your HA installation as a wifi hub
3. Once that's set, the [Home Assistant Community Store AKA HACS](https://hacs.xyz) will need to be installed, as many parts of this platform rely on community contributions to Home Assistant best accessed and updated this way. There's also [excellent documentation over on the HACS site](https://hacs.xyz/docs/setup/prerequisites) for getting this going.
4. Set up your Zigbee/Zwave radio if you're using one, and add the physical devices your installation will be using. It'll probably be helpful to use the naming convention of [Inst XXXX], with XXXX as the "id" of each YERP! instance.


### Setting up Home Assistant to work as a YERP! Installation

From here you can either clone this repo into your Home Assistant's config directory, or add sections piecemeal from this repo in a more piecemeal fashion.

The configuration.yaml file in this repo (in the .config/ folder in most HA installations) is the main config file for Home Assistant. The version included here uses another yaml file, secrets.yaml, pretty extensively (it's considered best practice to keep your more sensitive info like device login info, GPS coordinates, API keys etc here.. case in point, it's how this repo can include our configuration.yaml file without disclosing any of that), so you'll want to make one of these and cater it to your install.

There are a few more files in this repo that you'll want to include versions of in your install:

- **scenes.yaml** acts as a holder for various states smart bulbs should take during the YERP! spotting process.
- **scripts.yaml** which contains a script that resets a given YERP! instance.
- **sensors.yaml** creates some entities used to monitor an instance, including some an instances uses for calculations that run the spotting process
- **automations.yaml** which contains most of the working parts of an installation.

These all contain tags in the entity names as to which YERP! instance they're corresponding to. These files specifcally reference the development installation at Cool Industries, tagged in entity IDs with inst_cool and in entity names as [Inst Cool]. Doing a mass find and replace can adjust this to a tag suited to your installation, and is currently the same process to run multiple YERP! instances off of one Home Assistant installation (simply paste in multiple sets with different tags).

From here, you'll need to manually create the "helpers" on which YERP! also relies (to do: add a list of these). They're all referenced in the automations.yaml file, and are mostly counters.

You'll also want to edit references to a device in the YERP! automations with the Home Assistant app installed, for sending out notifications as to what's happening in a given YERP! instance. Searching "fluffphone" (hi it's me Michael, who often uses Fluffy / Fluff / Flufftronix as a handle) in automations.yaml should yield these automations, or in the HA Automations GUI they're listed by name as notifications. For testing purposes in the development installation they only go out to one phone, but using a different entity can alert all phones/tablets set up with a given installation. (Control over this via HA Dashboard is coming soon!) So edit this as appropriate for your install.

There are also some "virtual participant" automations, which are in here but not quite reliably functional yet. I'll leave the documentation here for once the functionality is up and running.

Finally, this leaves the interface by which you'll be most often interacting with YERP!, via Home Assistant's dashboard functionality. A few widgets are included here, which can be edited via the same find and replace tags you used earlier. To add these into your installation edit your dashboard, and paste these in as widgets.

You should now have an installation that's up to date with the current development version, ready for testing and experimentation. *(This is also the first version of an install walkthrough, so if there's anything that's missing please feel free to open an issue or submit a pull request!)*