import cryptocode

#coEZN87elfYmCgWk8kzhLUWVqAEZWk3bSkU4yfmV/4AisOZqfGviT+vQWe35e9FOrfxHmxoJM96pN6MFJBCnoSbOOumK9ZlKRSZM+uSLjJ4m00HKZ03hjJrrunNaclgFWQAx*dgc7K/ipH1HJSPSsEBBByQ==*G0hNBS/e3oEVWGtCQzlLbQ==*rAQ0xC1/LOfpO1zGV7LeBA==
cypher = input('Please enter your cypher text:')
#encoded = cryptocode.encrypt(plain_text,"mypassword")
## And then to decode it:
decoded = cryptocode.decrypt(cypher, "mypassword")

# print(encoded)
print(decoded)