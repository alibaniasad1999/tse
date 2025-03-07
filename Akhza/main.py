import pytse_client as tse
import matplotlib.pyplot as plt
import jdatetime

akhza_index = {
    906 : 17166179154270422,
    907 : 48771123304040433,
    908 : 17489918101053443,
    909 : 14925348052932291,
    910 : 40004156358768554,
    911 : 65985619452718369
}

today = jdatetime.date.today()
akhza_sarresid = {
    906 : jdatetime.date(1402,3,21) - today,
    907 : jdatetime.date(1402,7,4) - today,
    908 : jdatetime.date(1402,8,6) - today,
    909 : jdatetime.date(1402,3,16) - today,
    910 : jdatetime.date(1402,8,7) - today,
    911 : jdatetime.date(1402,9,6) - today,
}



akhze_data = []
for i in akhza_index:
    akhze_data.append(tse.Ticker("", index=str(akhza_index[i])))

for i in akhze_data:
    plt.plot(i.history.date[0:len(i.history.date)-1], i.history.open[0:len(i.history.open)-1])

plt.legend(['906', '907', '908', '909', '910', '911'])

best_buy = [0, 0, 0] # name and percent and price
for i in range(len(akhze_data)):
    print(i+906, int(akhze_data[i].best_supply_price), 'sod sal', (-int(akhze_data[i].best_supply_price) + 1000000) / akhza_sarresid[i+906].days * 365 / int(akhze_data[i].best_supply_price) * 100)
    if best_buy[1] < (-int(akhze_data[i].best_supply_price) + 1000000) / akhza_sarresid[i+906].days * 365 / int(akhze_data[i].best_supply_price) * 100:
        best_buy[2] = int(akhze_data[i].best_supply_price)
        best_buy[1] = (-int(akhze_data[i].best_supply_price) + 1000000) / akhza_sarresid[i+906].days * 365 / int(akhze_data[i].best_supply_price) * 100
        best_buy[0] = i + 906

print('**** Name:', best_buy[0], '*** Price ***', best_buy[2], '*** sod *** ', best_buy[1])


plt.show()
