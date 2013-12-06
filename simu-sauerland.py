#!/usr/bin/env python

import time
import json
import mosquitto

points = [
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806480471", "lon":"8.778893928" },
    { "lat" : "50.806588213", "lon":"8.778759195" },
    { "lat" : "50.806684818", "lon":"8.778678376" },
    { "lat" : "50.807721259", "lon":"8.778845195" },
    { "lat" : "50.808705028", "lon":"8.77899903" },
    { "lat" : "50.810482011", "lon":"8.779115676" },
    { "lat" : "50.812775125", "lon":"8.779045012" },
    { "lat" : "50.814733203", "lon":"8.777894303" },
    { "lat" : "50.816375189", "lon":"8.775805831" },
    { "lat" : "50.817950181", "lon":"8.773613593" },
    { "lat" : "50.819704029", "lon":"8.771931609" },
    { "lat" : "50.82157324", "lon":"8.770422203" },
    { "lat" : "50.823513865", "lon":"8.769014134" },
    { "lat" : "50.825870992", "lon":"8.767782006" },
    { "lat" : "50.828440951", "lon":"8.767044037" },
    { "lat" : "50.831263609", "lon":"8.766943857" },
    { "lat" : "50.834156904", "lon":"8.76758941" },
    { "lat" : "50.836919773", "lon":"8.769005539" },
    { "lat" : "50.839422728", "lon":"8.771275417" },
    { "lat" : "50.841224553", "lon":"8.774843594" },
    { "lat" : "50.841968102", "lon":"8.778829023" },
    { "lat" : "50.842205484", "lon":"8.782902733" },
    { "lat" : "50.843206193", "lon":"8.786921034" },
    { "lat" : "50.845330146", "lon":"8.790335032" },
    { "lat" : "50.847591919", "lon":"8.792571703" },
    { "lat" : "50.849708395", "lon":"8.794211402" },
    { "lat" : "50.851688337", "lon":"8.795360945" },
    { "lat" : "50.852983786", "lon":"8.796712902" },
    { "lat" : "50.854388231", "lon":"8.798097514" },
    { "lat" : "50.856046293", "lon":"8.797040313" },
    { "lat" : "50.856897733", "lon":"8.794233963" },
    { "lat" : "50.858200593", "lon":"8.792293925" },
    { "lat" : "50.859934405", "lon":"8.791619712" },
    { "lat" : "50.861659702", "lon":"8.791837382" },
    { "lat" : "50.86318198", "lon":"8.792161706" },
    { "lat" : "50.864790142", "lon":"8.792342503" },
    { "lat" : "50.86650489", "lon":"8.792161675" },
    { "lat" : "50.868239494", "lon":"8.791216277" },
    { "lat" : "50.869723639", "lon":"8.789604207" },
    { "lat" : "50.870871419", "lon":"8.787469001" },
    { "lat" : "50.871632158", "lon":"8.785181045" },
    { "lat" : "50.872660283", "lon":"8.783131926" },
    { "lat" : "50.873475252", "lon":"8.780742339" },
    { "lat" : "50.874086872", "lon":"8.778329851" },
    { "lat" : "50.874761624", "lon":"8.776575127" },
    { "lat" : "50.87476464", "lon":"8.775138574" },
    { "lat" : "50.87487803", "lon":"8.773850055" },
    { "lat" : "50.875966931", "lon":"8.773623866" },
    { "lat" : "50.876744279", "lon":"8.772435067" },
    { "lat" : "50.877378614", "lon":"8.770839989" },
    { "lat" : "50.878230951", "lon":"8.768830192" },
    { "lat" : "50.879522323", "lon":"8.767332538" },
    { "lat" : "50.880673023", "lon":"8.765581972" },
    { "lat" : "50.881387999", "lon":"8.763330988" },
    { "lat" : "50.882410201", "lon":"8.761484065" },
    { "lat" : "50.883605758", "lon":"8.759812119" },
    { "lat" : "50.884757628", "lon":"8.757914282" },
    { "lat" : "50.88570551", "lon":"8.755517178" },
    { "lat" : "50.886709751", "lon":"8.75317725" },
    { "lat" : "50.888089204", "lon":"8.751352621" },
    { "lat" : "50.889544167", "lon":"8.749743981" },
    { "lat" : "50.890536617", "lon":"8.748119013" },
    { "lat" : "50.891376929", "lon":"8.747235198" },
    { "lat" : "50.892057409", "lon":"8.747061251" },
    { "lat" : "50.892526634", "lon":"8.746128766" },
    { "lat" : "50.892940127", "lon":"8.744867781" },
    { "lat" : "50.893875735", "lon":"8.743675902" },
    { "lat" : "50.895214705", "lon":"8.742159766" },
    { "lat" : "50.896678222", "lon":"8.740492243" },
    { "lat" : "50.898079265", "lon":"8.738884063" },
    { "lat" : "50.899435715", "lon":"8.737454109" },
    { "lat" : "50.900644592", "lon":"8.736329943" },
    { "lat" : "50.901634395", "lon":"8.735036094" },
    { "lat" : "50.902350146", "lon":"8.733758479" },
    { "lat" : "50.902936863", "lon":"8.732447352" },
    { "lat" : "50.903628311", "lon":"8.731097251" },
    { "lat" : "50.904269179", "lon":"8.729893041" },
    { "lat" : "50.90457042", "lon":"8.729329841" },
    { "lat" : "50.904626523", "lon":"8.729205538" },
    { "lat" : "50.905015144", "lon":"8.728234845" },
    { "lat" : "50.905593492", "lon":"8.727201337" },
    { "lat" : "50.906229864", "lon":"8.726297469" },
    { "lat" : "50.907130276", "lon":"8.725492915" },
    { "lat" : "50.908202002", "lon":"8.724742312" },
    { "lat" : "50.909440456", "lon":"8.723448972" },
    { "lat" : "50.91095057", "lon":"8.721777087" },
    { "lat" : "50.912806488", "lon":"8.719886528" },
    { "lat" : "50.914354946", "lon":"8.717442535" },
    { "lat" : "50.915776141", "lon":"8.714942263" },
    { "lat" : "50.916696766", "lon":"8.712536253" },
    { "lat" : "50.917214919", "lon":"8.709990964" },
    { "lat" : "50.918337303", "lon":"8.708207303" },
    { "lat" : "50.919822906", "lon":"8.707514129" },
    { "lat" : "50.921110664", "lon":"8.706632981" },
    { "lat" : "50.922132438", "lon":"8.705585514" },
    { "lat" : "50.923096928", "lon":"8.705205165" },
    { "lat" : "50.924071021", "lon":"8.704923206" },
    { "lat" : "50.962177135", "lon":"8.717573267" },
    { "lat" : "50.962177135", "lon":"8.717573267" },
    { "lat" : "50.962594307", "lon":"8.718210406" },
    { "lat" : "50.963152125", "lon":"8.719570341" },
    { "lat" : "50.96414763", "lon":"8.720862993" },
    { "lat" : "50.965237082", "lon":"8.722241157" },
    { "lat" : "50.966533276", "lon":"8.723257809" },
    { "lat" : "50.96810962", "lon":"8.723745132" },
    { "lat" : "50.969545697", "lon":"8.724386225" },
    { "lat" : "50.970920749", "lon":"8.725294779" },
    { "lat" : "50.972301836", "lon":"8.725240039" },
    { "lat" : "50.973401878", "lon":"8.725669243" },
    { "lat" : "50.97440824", "lon":"8.726628893" },
    { "lat" : "50.975617277", "lon":"8.727188014" },
    { "lat" : "50.976770731", "lon":"8.727659515" },
    { "lat" : "50.977551111", "lon":"8.728485145" },
    { "lat" : "50.978346736", "lon":"8.729558692" },
    { "lat" : "50.979231527", "lon":"8.730649566" },
    { "lat" : "50.980217263", "lon":"8.731320431" },
    { "lat" : "50.981134344", "lon":"8.73196428" },
    { "lat" : "50.981939297", "lon":"8.732895065" },
    { "lat" : "50.982772209", "lon":"8.733904903" },
    { "lat" : "50.983608111", "lon":"8.734856317" },
    { "lat" : "50.984362289", "lon":"8.736066536" },
    { "lat" : "50.984686739", "lon":"8.737744585" },
    { "lat" : "50.985780751", "lon":"8.738928846" },
    { "lat" : "50.987076266", "lon":"8.740234403" },
    { "lat" : "50.988537342", "lon":"8.741406839" },
    { "lat" : "50.990085469", "lon":"8.742586917" },
    { "lat" : "50.991572206", "lon":"8.743774653" },
    { "lat" : "50.992600879", "lon":"8.745655493" },
    { "lat" : "50.99270929", "lon":"8.748508781" },
    { "lat" : "50.992781529", "lon":"8.75161546" },
    { "lat" : "50.992696029", "lon":"8.754731858" },
    { "lat" : "50.992793904", "lon":"8.757983639" },
    { "lat" : "50.993970937", "lon":"8.761135066" },
    { "lat" : "50.996032941", "lon":"8.764061764" },
    { "lat" : "50.998324672", "lon":"8.76677328" },
    { "lat" : "51.000038715", "lon":"8.769289826" },
    { "lat" : "51.000914513", "lon":"8.771672908" },
    { "lat" : "51.001915604", "lon":"8.773931634" },
    { "lat" : "51.003392471", "lon":"8.774910514" },
    { "lat" : "51.004928715", "lon":"8.775198428" },
    { "lat" : "51.006064926", "lon":"8.776941861" },
    { "lat" : "51.006342094", "lon":"8.779685638" },
    { "lat" : "51.005877688", "lon":"8.782382264" },
    { "lat" : "51.005342312", "lon":"8.785025712" },
    { "lat" : "51.004992555", "lon":"8.787662836" },
    { "lat" : "51.00573148", "lon":"8.790130972" },
    { "lat" : "51.007225696", "lon":"8.791420322" },
    { "lat" : "51.008951184", "lon":"8.791654926" },
    { "lat" : "51.010585061", "lon":"8.793078843" },
    { "lat" : "51.012499312", "lon":"8.795838849" },
    { "lat" : "51.014581107", "lon":"8.798924305" },
    { "lat" : "51.016600245", "lon":"8.80186586" },
    { "lat" : "51.018194303", "lon":"8.804148403" },
    { "lat" : "51.051089264", "lon":"8.815457647" },
    { "lat" : "51.05295268", "lon":"8.816687851" },
    { "lat" : "51.0548782", "lon":"8.81806783" },
    { "lat" : "51.05687553", "lon":"8.8191714" },
    { "lat" : "51.058897734", "lon":"8.819575703" },
    { "lat" : "51.060937675", "lon":"8.819319776" },
    { "lat" : "51.062992378", "lon":"8.818404504" },
    { "lat" : "51.064960499", "lon":"8.816934797" },
    { "lat" : "51.066843016", "lon":"8.815345632" },
    { "lat" : "51.068772913", "lon":"8.813839936" },
    { "lat" : "51.070873873", "lon":"8.813321411" },
    { "lat" : "51.072869817", "lon":"8.81424211" },
    { "lat" : "51.074527458", "lon":"8.815837013" },
    { "lat" : "51.075694981", "lon":"8.817256555" },
    { "lat" : "51.076441927", "lon":"8.819000958" },
    { "lat" : "51.077083741", "lon":"8.820601987" },
    { "lat" : "51.077266523", "lon":"8.820930901" },
    { "lat" : "51.077266523", "lon":"8.820930901" },
    { "lat" : "51.077805433", "lon":"8.821634687" },
    { "lat" : "51.079223109", "lon":"8.822590633" },
    { "lat" : "51.080809651", "lon":"8.824320496" },
    { "lat" : "51.082234306", "lon":"8.826524314" },
    { "lat" : "51.083818489", "lon":"8.828654615" },
    { "lat" : "51.085556971", "lon":"8.831005627" },
    { "lat" : "51.11084855", "lon":"8.852106099" },
    { "lat" : "51.112615773", "lon":"8.855153253" },
    { "lat" : "51.114099664", "lon":"8.858392128" },
    { "lat" : "51.114367914", "lon":"8.862457535" },
    { "lat" : "51.114696795", "lon":"8.865969614" },
    { "lat" : "51.114867118", "lon":"8.869075275" },
    { "lat" : "51.114961509", "lon":"8.87217305" },
    { "lat" : "51.11571132", "lon":"8.875035764" },
    { "lat" : "51.117098733", "lon":"8.876826636" },
    { "lat" : "51.118827599", "lon":"8.876426558" },
    { "lat" : "51.120528238", "lon":"8.876230613" },
    { "lat" : "51.122343773", "lon":"8.875493123" },
    { "lat" : "51.124007863", "lon":"8.873997092" },
    { "lat" : "51.125784543", "lon":"8.873563322" },
    { "lat" : "51.127598555", "lon":"8.874028768" },
    { "lat" : "51.129108489", "lon":"8.875696573" },
    { "lat" : "51.130398466", "lon":"8.877615895" },
    { "lat" : "51.131582958", "lon":"8.879620889" },
    { "lat" : "51.132892074", "lon":"8.881678475" },
    { "lat" : "51.134428545", "lon":"8.883481684" },
    { "lat" : "51.136174914", "lon":"8.884777322" },
    { "lat" : "51.138217874", "lon":"8.885428603" },
    { "lat" : "51.140935891", "lon":"8.885757095" },
    { "lat" : "51.143648899", "lon":"8.886192402" },
    { "lat" : "51.146129586", "lon":"8.88735616" },
    { "lat" : "51.148045186", "lon":"8.889802115" },
    { "lat" : "51.149524637", "lon":"8.89275425" },
    { "lat" : "51.151105655", "lon":"8.895046517" },
    { "lat" : "51.15263087", "lon":"8.896921484" },
    { "lat" : "51.153784448", "lon":"8.899198424" },
    { "lat" : "51.154616723", "lon":"8.901793949" },
    { "lat" : "51.155344261", "lon":"8.904278301" },
    { "lat" : "51.156550834", "lon":"8.906285053" },
    { "lat" : "51.158248126", "lon":"8.907479747" },
    { "lat" : "51.16018869", "lon":"8.907804788" },
    { "lat" : "51.162170859", "lon":"8.907312976" },
    { "lat" : "51.163918775", "lon":"8.905930326" },
    { "lat" : "51.165110518", "lon":"8.903609768" },
    { "lat" : "51.166355277", "lon":"8.901535826" },
    { "lat" : "51.167478202", "lon":"8.899334152" },
    { "lat" : "51.168325638", "lon":"8.896832554" },
    { "lat" : "51.169269676", "lon":"8.894658437" },
    { "lat" : "51.17074615", "lon":"8.893528367" },
    { "lat" : "51.172436784", "lon":"8.893277209" },
    { "lat" : "51.174137418", "lon":"8.892765123" },
    { "lat" : "51.175631413", "lon":"8.891479475" },
    { "lat" : "51.176909689", "lon":"8.88950055" },
    { "lat" : "51.178217365", "lon":"8.887469421" },
    { "lat" : "51.179922905", "lon":"8.886949559" },
    { "lat" : "51.181667807", "lon":"8.887819189" },
    { "lat" : "51.183295131", "lon":"8.88937681" },
    { "lat" : "51.184039571", "lon":"8.891683246" },
    { "lat" : "51.184600325", "lon":"8.893357374" },
    { "lat" : "51.185532122", "lon":"8.894484525" },
    { "lat" : "51.186588431", "lon":"8.894925972" },
    { "lat" : "51.187915054", "lon":"8.895032356" },
    { "lat" : "51.189622729", "lon":"8.895260758" },
    { "lat" : "51.19097933", "lon":"8.893536197" },
    { "lat" : "51.191346036", "lon":"8.890604288" },
    { "lat" : "51.192631633", "lon":"8.888972685" },
    { "lat" : "51.194447267", "lon":"8.889528625" },
    { "lat" : "51.196130829", "lon":"8.888645141" },
    { "lat" : "51.197561616", "lon":"8.887369337" },
    { "lat" : "51.198570518", "lon":"8.887304995" },
    { "lat" : "51.199253315", "lon":"8.887416841" },
    { "lat" : "51.199360657", "lon":"8.887436733" },
    { "lat" : "51.199360657", "lon":"8.887436733" },
    { "lat" : "51.199360657", "lon":"8.887436733" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
    { "lat" : "51.199332421", "lon":"8.887337328" },
]

topic = 'mqttitude/sim/sauer'

mqttc = mosquitto.Mosquitto(clean_session=True)
mqttc.connect("localhost", 1883, 60)

for n in points:
    lat = n['lat']
    lon = n['lon']
    tst = int(time.time())

    item = {
        'lat' : lat,
        'lon' : lon,
        'tst' : tst,
        '_type' : 'location'
    }

    payload = json.dumps(item)

    (res, mid) = mqttc.publish(topic, payload, qos=1, retain=False)
    rc = mqttc.loop()
    if rc != 0:
        print "ERROR"
        sys.exit(1)

    time.sleep(0.3)

