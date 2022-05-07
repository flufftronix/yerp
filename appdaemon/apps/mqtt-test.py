import appdaemon.plugins.hass.hassapi as hass

class test_Mqtt(hass.Hass):
    def initialize(self):
        mqtt = self.get_plugin_api("MQTT")
        mqtt.mqtt_subscribe(topic=your_topic)      
        mqtt.listen_event(self.cb_event, "MQTT_MESSAGE", topic=your_topic, namespace='mqtt')
		
    def cb_event(self, event_name, data, kwargs):
	    self.log(data)