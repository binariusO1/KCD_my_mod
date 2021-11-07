
Horsetraders = {}

Horsetraders.__data__ = 
{
	stables = 
	{
		['aus'] = 
		{
			merchants = 
			{
				'aus_groom'
			},
			
			horses =
			{
				[1] = 
				{
					name = 'horse_stablesAus_01'
				},
				
				[2] = 
				{
					name = 'horse_stablesAus_02'
				},
				
				[3] = 
				{
					name = 'horse_stablesAus_03'
				},
				
				[4] = 
				{
					name = 'horse_stablesAus_04'
				},
				
				[5] = 
				{
					name = 'horse_stablesAus_05'
				},
			}
		},
		
		
		['mrh'] = 
		{
			merchants = 
			{
				'mrh_johan'
			},
			
			horses =
			{
				[1] = 
				{
					name = 'horse_stablesMrh_01'
				},
				
				[2] = 
				{
					name = 'horse_stablesMrh_02'
				},
				
				[3] = 
				{
					name = 'horse_stablesMrh_03'
				},
				
				[4] = 
				{
					name = 'horse_stablesMrh_04'
				},
				
				[5] = 
				{
					name = 'horse_stablesMrh_05'
				},
			}
		},
		
		['neu'] = 
		{
			merchants = 
			{
				'neu_zdena'
			},
			
			horses =
			{
				[1] = 
				{
					name = 'horse_stablesNeu_01'
				},
				
				[2] = 
				{
					name = 'horse_stablesNeu_02'
				},
				
				[3] = 
				{
					name = 'horse_stablesNeu_03'
				},
				
				[4] = 
				{
					name = 'horse_stablesNeu_04'
				},
				
				[5] = 
				{
					name = 'horse_stablesNeu_05'
				},
				
				[6] = 
				{
					name = 'horse_stablesNeu_06'
				},
				
				[7] = 
				{
					name = 'horse_stablesNeu_07'
				},
				
				[8] = 
				{
					name = 'horse_stablesNeu_08'
				},
				
				[9] = 
				{
					name = 'horse_stablesNeu_09'
				},
				
				[10] = 
				{
					name = 'horse_stablesNeu_10'
				},
			}
		},
		
		['prib'] = 
		{
			merchants = 
			{
				'prib_stableman', 'aus_vasek', 'neu_marek'
			},
			
			horses =
			{
				[1] = 
				{
					name = 'horse_stablesPrib_01'
				},
				
				[2] = 
				{
					name = 'horse_stablesPrib_02'
				},
				
				[3] = 
				{
					name = 'horse_stablesPrib_03'
				}
			}
		},
		
		['other'] = 
		{
			merchants = 
			{
			},
			
			horses =
			{
				[1] = 
				{
					name = 'horse_sedivka',
					despawnWhenSold = true,
					price = 500
				},
				
				[2] = 
				{
					name = 'gamblers_den_bandit_chief_horse',
					despawnWhenSold = true
				}
			}
		},
	}
}

function Horsetraders.calcPrices()
	
	local stats = { 'agi', 'cou', 'str', 'vit' }
	
	local horseWithMinStatsPrice = RPG.HorseWithMinStatsPrice
	local horseWithMaxStatsPrice = RPG.HorseWithMaxStatsPrice
	local minResultPrice = RPG.HorseMinFinalPrice 
	local statCap = RPG.StatCap
	
	for stableCode, stableData in pairs(Horsetraders.__data__.stables) do
	
		for _, horseData in pairs(stableData.horses) do
		
			if horseData.price == nil then
		
				local entity = System.GetEntityByName(horseData.name)
				if entity ~= nil then
				
					local sum = 0
					for _, stat in ipairs(stats) do
				
						local level = entity.soul:GetStatLevel(stat)
						if isNumber(level) then
						
							sum = sum + level
						
						else
						
							TError(strFormat("Cannot retrieve stat '%s' on horse '%s'", stat, horseData.name))
						
						end
				
					end
														
					local average = (sum / statCap) / #stats
					local price = math.lerp(horseWithMinStatsPrice, horseWithMaxStatsPrice, average)
					local step = 10
					price = math.round(price / step) * step
					price = math.max(price, minResultPrice)
					horseData.price = price * 10
					
				end
				
			end
		
		end
	
	end
	
end
function Horsetraders.setContextMerchant (merchant)

	for stableCode, stableData in pairs(Horsetraders.__data__.stables) do
	
		if table.contains(stableData.merchants, merchant.this.name) then
		
			Horsetraders.contextMerchant = merchant
			Horsetraders.contextStables = stableCode
			return
		
		end
	
	end
	
	error("Invalid horsetrader merchant -- cannot determine stables")

end

function Horsetraders.clearContext()

	Horsetraders.contextMerchant = nil
	Horsetraders.contextStables = nil

end
function Horsetraders.exp_isHorseAvailableToPurchase (horseStableCodeAndIndex)

	local stables, horseIndex = horseStableCodeAndIndex:match('(%a+)-(%d+)')
	assert(stables, strFormat("Cannot parse '%s' as a stables code and horse index", horseStableCodeAndIndex))
	horseIndex = tonumber(horseIndex)
	local stablesData = Horsetraders.__data__.stables[stables]
	assert(stablesData, strFormat("Invalid stable code '%s'", stables))
	
	local horseData = stablesData.horses[horseIndex]
	assert(horseData, strFormat("Invalid combination: stables code '%s' and horse index '%d'", stables, horseIndex))
	if stables ~= Horsetraders.contextStables then
	
		return 0
	
	end
	local horse = System.GetEntityByName(horseData.name)
	if horse == nil then
	
		TError(strFormat("Cannot find horse entity '%s'", horseData.name))
		return 0
	
	end
	local currentPos = player:GetPos()
	local horsePos = horse:GetPos()
	if math.dist({ currentPos.x, currentPos.y, currentPos.z }, { horsePos.x, horsePos.y, horsePos.z }) > 400 then
	
		return 0
	
	end
	if horse.soul:GetState('health') <= 0 then
	
		return 0
		
	end
	local horse = Horsetraders.getPlayerHorse()
	if horse and horse.this.name == horseData.name then
	
		return 0
		
	end
	
	return 1
	
end
function Horsetraders.setContextHorse (horse)

	Horsetraders.contextHorse = horse

end

function Horsetraders.setupDealTopicData()
	local stablesData = Horsetraders.__data__.stables[Horsetraders.contextStables]
	assert(stablesData, "Cannot setup deal conditions without a valid context stables code")
	
	local horseData = stablesData.horses[Horsetraders.contextHorse]
	assert(horseData, "Cannot setup deal conditions without a valid context horse")
	local playerHorse = Horsetraders.getPlayerHorse()
	local playerReputationModifier = Horsetraders.getPlayerReputationModifier()
	if Horsetraders.selectedHorsePrice == nil then
	
		local price = Horsetraders.getHorsePrice(horseData.name)
		Horsetraders.selectedHorsePrice = Horsetraders.calcSellingPrice(price) * playerReputationModifier
		
	end
	if (playerHorse ~= nil) and (Horsetraders.playerHorsePrice == nil) then
	
		local price = Horsetraders.getHorsePrice(playerHorse.this.name)
		Horsetraders.playerHorsePrice = Horsetraders.calcBuyingPrice(price) / playerReputationModifier
	
	end
	local price = Horsetraders.selectedHorsePrice
	if Horsetraders.counterOfferMade then	
	
		price = price - Horsetraders.playerHorsePrice
	
	end
	price = Horsetraders.roundTotalPrice(price)
	Utils.SetLocalVar('price', price)
	Variables.SetGlobal('dlg_crimeFineAmount', math.abs(price) / 10)
	Variables.SetGlobal('dlg_crimeFineShown', 1)
	if (playerHorse ~= nil) and (not Horsetraders.counterOfferMade) then
		Utils.SetLocalVar('horsetraders_dealTopic_showPlayerCounterofferOption', 1)
		
	else
		if price > 0 then
			if player.inventory:GetMoney() * 10 >= price then
			
				Utils.SetLocalVar('horsetraders_dealTopic_showAcceptOption_pay', 1)
			
			end
		else
		
			Utils.SetLocalVar('horsetraders_dealTopic_showAcceptOption_receive', 1)
		
		end
		Utils.SetLocalVar('horsetraders_dealTopic_showHaggleOption', 1)
		NegotiationUtils.SetupNegotiation(NegotiationReason.Horsetrader, Horsetraders.selectedHorsePrice, Horsetraders.playerHorsePrice or 0, 0, 0)
		Utils.SetLocalVar('horsetraders_dealTopic_showPlayerCounterofferOption', 0)
		
	end
	
end

function Horsetraders.clearDealTopicData()

	Utils.SetLocalVar('horsetraders_dealTopic_showPlayerCounterofferOption', 0)
	Utils.SetLocalVar('horsetraders_dealTopic_showAcceptOption_pay', 0)
	Utils.SetLocalVar('horsetraders_dealTopic_showAcceptOption_receive', 0)	
	Utils.SetLocalVar('horsetraders_dealTopic_showHaggleOption', 0)
	
	Variables.SetGlobal('dlg_crimeFineAmount', 0)
	Variables.SetGlobal('dlg_crimeFineShown', 0)
	
	Horsetraders.playerHorsePrice = nil
	Horsetraders.selectedHorsePrice = nil
	Horsetraders.counterOfferMade = nil	
	
end

function Horsetraders.makeCounterOffer()
	
	Horsetraders.counterOfferMade = true

end

function Horsetraders.getHorsePrice (name)

	local horseData = assert(Horsetraders.getHorseDataByHorseName(name), strFormat("Cannot find horse data for horse '%s'", name))
	if horseData.price == nil then
	
		Horsetraders.calcPrices()
		
	end
	
	return horseData.price

end

function Horsetraders.getHorseDataByHorseName (name)

	for stableCode, stableData in pairs(Horsetraders.__data__.stables) do
	
		for _, horseData in pairs(stableData.horses) do
		
			if horseData.name == name then
			
				return horseData
			
			end
		
		end
	
	end

end
function Horsetraders.calcSellingPrice (price)

	return price * 1.3

end
function Horsetraders.calcBuyingPrice (price)

	return price * 0.4

end
function Horsetraders.getPlayerReputationModifier()
	
	local scale = 0.2
	local relationship = Horsetraders.contextMerchant.soul:GetRelationship(player.this.id)
	return 1 + 2 * (0.5 - relationship) * scale

end

function Horsetraders.roundTotalPrice (price)

	local step = 100
	return math.round(price / step) * step

end

function Horsetraders.getPlayerHorse()

	local horse = player.player:GetPlayerHorse()
	if horse == __null then
	
		return nil
		
	end
	
	horse = XGenAIModule.GetEntityByWUID(horse)
	if horse == nil then
	
		error("Cannot locate player's horse entity")
	
	end
	
	return horse

end

function Horsetraders.makeDeal (price)
	local stablesData = Horsetraders.__data__.stables[Horsetraders.contextStables]
	assert(stablesData, "Cannot setup deal conditions without a valid context stables code")
	
	local horseData = stablesData.horses[Horsetraders.contextHorse]
	assert(horseData, "Cannot setup deal conditions without a valid context horse")	
	
	local newHorse = assert(System.GetEntityByName(horseData.name), strFormat("Cannot find entity '%s'.", horseData.name))
	Horsetraders.clearDealTopicData()
	if newHorse.soul:GetState('health') <= 0 then

		return nil

	end
	if price > 0 then
	
		Utils.RemoveInvItem(player, Utils.itemIDs.money, price)
		
	else
	
		local item = ItemManager.CreateItem(Utils.itemIDs.money, 1, -price)
		player.inventory:AddItem(item);
	
	end

		
	Horsetraders.setNewPlayerHorse(horseData.name)
	
end

function Horsetraders.setNewPlayerHorse (name)
	local message = {}
	
	local newHorse = assert(System.GetEntityByName(name), strFormat("Cannot find entity '%s'.", name))
	message.boughtHorse = newHorse.this.id	

	local playerHorse = Horsetraders.getPlayerHorse()
	if playerHorse ~= nil then
	
		message.soldHorse = playerHorse.this.id
		
		local playerHorseData = Horsetraders.getHorseDataByHorseName(playerHorse.this.name)
		message.despawnSoldHorse = playerHorseData.despawnWhenSold
		
	else
	
		message.soldHorse = __null
		message.despawnSoldHorse = false
	
	end
	
	XGenAIModule.SendMessageToEntityData(player.this.id, 'horsetraders:deal', message)
	player.player:SetPlayerHorse(newHorse.id)
	
end