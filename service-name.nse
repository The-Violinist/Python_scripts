 GNU nano 5.3                                                                                                    portscan.nse *                                                                                                           
-- HEAD --

description = [[
This script returns the service names.
]]

author = "David Armstrong"

-- RULE --

portrule = function(host, port)
        return port.protocol == "tcp"
end

-- ACTION --

action = function(host, port)
        return print(port.version.name)
        
end
