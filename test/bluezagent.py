import dbus
import logging

BUS_NAME = 'org.bluez'
AGENT_INTERFACE = 'org.bluez.Agent1'

class Agent(dbus.service.Object):

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="", out_signature="")
	def Release(self):
		logging.info("Release")

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="os", out_signature="")
	def AuthorizeService(self, device, uuid):
		logging.info("AuthorizeService (%s, %s)" % (device, uuid))

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="o", out_signature="s")
	def RequestPinCode(self, device):
		logging.info("RequestPinCode (%s)" % (device))

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="o", out_signature="u")
	def RequestPasskey(self, device):
		logging.info("RequestPasskey (%s)" % (device))

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="ouq", out_signature="")
	def DisplayPasskey(self, device, passkey, entered):
		logging.info("DisplayPasskey (%s, %06u entered %u)" %
						(device, passkey, entered))

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="os", out_signature="")
	def DisplayPinCode(self, device, pincode):
		logging.info("DisplayPinCode (%s, %s)" % (device, pincode))

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="ou", out_signature="")
	def RequestConfirmation(self, device, passkey):
		logging.info("RequestConfirmation (%s, %06d)" % (device, passkey))

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="o", out_signature="")
	def RequestAuthorization(self, device):
		logging.info("RequestAuthorization (%s)" % (device))

	@dbus.service.method(AGENT_INTERFACE,
					in_signature="", out_signature="")
	def Cancel(self):
		logging.info("Cancel")

# Start a Default Agent for connect request
# bus: a open dbus handle
# agent_path: any path
# capability: NoInputNoOutput/DisplayYesNo/DisplayOnly/KeyboardOnly/KeyboardDisplay
def StartDefaultAgent(bus, agent_path, capability='NoInputNoOutput'):
	agent = Agent(bus, agent_path)
	manager = dbus.Interface(bus.get_object(BUS_NAME, '/org/bluez'),
							'org.bluez.AgentManager1')
	manager.RegisterAgent(agent_path, capability)
	manager.RequestDefaultAgent(agent_path)
	logging.info('Default Agent Registered')


