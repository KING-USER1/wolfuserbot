# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Credits @Smart_S54.

from covid import Covid
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Wait Processing...π₯Ίπ­`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        output_text = (
            f"π€ **Confirmed   :** `{country_data['confirmed']}`\n" +
            f"π **Active      :** `{country_data['active']}`\n" +
            f"π **Deaths      :** `{country_data['deaths']}`\n" +
            f"π **Recovered   :** `{country_data['recovered']}`\n\n" +
            f"π **New Cases   :** `{country_data['new_cases']}`\n" +
            f"π­ **New Deaths  :** `{country_data['new_deaths']}`\n" +
            f"π₯ **Critical    :** `{country_data['critical']}`\n" +
            f"π **Total Tests :** `{country_data['total_tests']}`\n\n" +
            f"π **Data provided by** [Worldometer](https://www.worldometers.info/coronavirus/country/{country})")
        await event.edit(f"__**π¦  Corona Virus Info in {country}:**__\n\n{output_text}")
    except ValueError:
        await event.edit(
            f"__**π€ No information found for: {country}!**__\n__**Check your spelling and try again.**__"
        )


CMD_HELP.update({
    "covid":
        "`.covid` <country>"
        "\nUsage: Get an information about data covid-19 in your country.\n"
})
