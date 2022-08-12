from mcquery import mcquery

def query(ip, port):
    with mcquery(ip, port=port, timeout=10) as data:
        hostname = data.hostname
        game_type = data.game_type
        game_id = data.game_id
        version = data.version
        server_engine = data.server_engine
        plugins = data.plugins
        map = data.map
        num_players = str(data.num_players)
        max_players = str(data.max_players)
        whitelist = data.whitelist
        host_ip = data.host_ip
        host_port = str(data.host_port)
        # You can create an embed for discord if you want
        print(hostname)
        print(game_type)
        print(game_id)
        print(version)
        print(server_engine)
        print(", ".join(plugins))
        print(map)
        print(num_players)
        print(max_players)
        print(whitelist)
        print(host_ip)
        print(host_port)

query("play.nethergames.org", 19132)
