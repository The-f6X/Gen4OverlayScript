--Original code by KazoWAR over here https://projectpokemon.org/home/forums/topic/30518-4th-and-5th-gen-misc-info-reading-scripts/
file = io.open("team.txt", "w")
local PartyOffset
local BattleOfffset
local SeenOffset
local OwnOffset
local Seed
local PKMNumber
local PID
local BlockOrder
local DecryptedOffset
local DecryptedData
local DecryptedPKMData = {}
local EncryptedOffset
local EncryptedData
local EncryptedPKMData = {}
local ID = {}
local HP = {}
local MAXHP = {}
local Lvl = {}
local Move1 = {}
local Move2 = {}
local Move3 = {}
local Move4 = {}
local PP1 = {}
local PP2 = {}
local PP3 = {}
local PP4 = {}
local MAXPP1 = {}
local MAXPP2 = {}
local MAXPP3 = {}
local MAXPP4 = {}
local Status = {}
local Gender = {}
local Egg = {}
local ID2 = {}
local HP2 = {}
local MAXHP2 = {}
local Lvl2 = {}
local Move1_2 = {}
local Move2_2 = {}
local Move3_2 = {}
local Move4_2 = {}
local PP1_2 = {}
local PP2_2 = {}
local PP3_2 = {}
local PP4_2 = {}
local MAXPP1_2 = {}
local MAXPP2_2 = {}
local MAXPP3_2 = {}
local MAXPP4_2 = {}
local Status2 = {}
local Gender2 = {}
local Egg2 = {}
local Valid
local BadgeSet1
local BadgeSet2
local BadgeData = {}
local Money
local Seen
local Own
local Checksum
local MapID
local PPVal = { 0x23, 0x19, 0x0A, 0x0F, 0x14, 0x14, 0x0F, 0x0F, 0x0F, 0x23, 0x1E, 0x05, 0x0A, 0x1E, 0x1E, 0x23, 0x23, 0x14, 0x0F, 0x14, 0x14, 0x0F, 0x14, 0x1E, 0x05, 0x0A, 0x0F, 0x0F, 0x0F, 0x19, 0x14, 0x05, 0x23, 0x0F, 0x14, 0x14, 0x0A, 0x0F, 0x1E, 0x23, 0x14, 0x14, 0x1E, 0x19, 0x28, 0x14, 0x0F, 0x14, 0x14, 0x14, 0x1E, 0x19, 0x0F, 0x1E, 0x19, 0x05, 0x0F, 0x0A, 0x05, 0x14, 0x14, 0x14, 0x05, 0x23, 0x14, 0x19, 0x14, 0x14, 0x14, 0x0F, 0x19, 0x0F, 0x0A, 0x28, 0x19, 0x0A, 0x23, 0x1E, 0x0F, 0x0A, 0x28, 0x0A, 0x0F, 0x1E, 0x0F, 0x14, 0x0A, 0x0F, 0x0A, 0x05, 0x0A, 0x0A, 0x19, 0x0A, 0x14, 0x28, 0x1E, 0x1E, 0x14, 0x14, 0x0F, 0x0A, 0x28, 0x0F, 0x0A, 0x1E, 0x14, 0x14, 0x0A, 0x28, 0x28, 0x1E, 0x1E, 0x1E, 0x14, 0x1E, 0x0A, 0x0A, 0x14, 0x05, 0x0A, 0x1E, 0x14, 0x14, 0x14, 0x05, 0x0F, 0x0F, 0x14, 0x0F, 0x0F, 0x23, 0x14, 0x0F, 0x0A, 0x0A, 0x1E, 0x0F, 0x28, 0x14, 0x0F, 0x0A, 0x05, 0x0A, 0x1E, 0x0A, 0x0F, 0x14, 0x0F, 0x28, 0x28, 0x0A, 0x05, 0x0F, 0x0A, 0x0A, 0x0A, 0x0F, 0x1E, 0x1E, 0x0A, 0x0A, 0x14, 0x0A, 0x01, 0x01, 0x0A, 0x0A, 0x0A, 0x05, 0x0F, 0x19, 0x0F, 0x0A, 0x0F, 0x1E, 0x05, 0x28, 0x0F, 0x0A, 0x19, 0x0A, 0x1E, 0x0A, 0x14, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x14, 0x05, 0x28, 0x05, 0x05, 0x0F, 0x05, 0x0A, 0x05, 0x0A, 0x0A, 0x0A, 0x0A, 0x14, 0x14, 0x28, 0x0F, 0x0A, 0x14, 0x14, 0x19, 0x05, 0x0F, 0x0A, 0x05, 0x14, 0x0F, 0x14, 0x19, 0x14, 0x05, 0x1E, 0x05, 0x0A, 0x14, 0x28, 0x05, 0x14, 0x28, 0x14, 0x0F, 0x23, 0x0A, 0x05, 0x05, 0x05, 0x0F, 0x05, 0x14, 0x05, 0x05, 0x0F, 0x14, 0x0A, 0x05, 0x05, 0x0F, 0x0A, 0x0F, 0x0F, 0x0A, 0x0A, 0x0A, 0x14, 0x0A, 0x0A, 0x0A, 0x0A, 0x0F, 0x0F, 0x0F, 0x0A, 0x14, 0x14, 0x0A, 0x14, 0x14, 0x14, 0x14, 0x14, 0x0A, 0x0A, 0x0A, 0x14, 0x14, 0x05, 0x0F, 0x0A, 0x0A, 0x0F, 0x0A, 0x14, 0x05, 0x05, 0x0A, 0x0A, 0x14, 0x05, 0x0A, 0x14, 0x0A, 0x14, 0x14, 0x14, 0x05, 0x05, 0x0F, 0x14, 0x0A, 0x0F, 0x14, 0x0F, 0x0A, 0x0A, 0x0F, 0x0A, 0x05, 0x05, 0x0A, 0x0F, 0x0A, 0x05, 0x14, 0x19, 0x05, 0x28, 0x0A, 0x05, 0x28, 0x0F, 0x14, 0x14, 0x05, 0x0F, 0x14, 0x1E, 0x0F, 0x0F, 0x05, 0x0A, 0x1E, 0x14, 0x1E, 0x0F, 0x05, 0x28, 0x0F, 0x05, 0x14, 0x05, 0x0F, 0x19, 0x28, 0x0F, 0x14, 0x0F, 0x14, 0x0F, 0x14, 0x0A, 0x14, 0x14, 0x05, 0x05, 0x0A, 0x05, 0x28, 0x0A, 0x0A, 0x05, 0x0A, 0x0A, 0x0F, 0x0A, 0x14, 0x1E, 0x1E, 0x0A, 0x14, 0x05, 0x0A, 0x0A, 0x0F, 0x0A, 0x0A, 0x05, 0x0F, 0x05, 0x0A, 0x0A, 0x1E, 0x14, 0x14, 0x0A, 0x0A, 0x05, 0x05, 0x0A, 0x05, 0x14, 0x0A, 0x14, 0x0A, 0x0F, 0x0A, 0x14, 0x14, 0x14, 0x0F, 0x0F, 0x0A, 0x0F, 0x14, 0x0F, 0x0A, 0x0A, 0x0A, 0x14, 0x0A, 0x1E, 0x05, 0x0A, 0x0F, 0x0A, 0x0A, 0x05, 0x14, 0x1E, 0x0A, 0x1E, 0x0F, 0x0F, 0x0F, 0x0F, 0x1E, 0x0A, 0x14, 0x0F, 0x0A, 0x0A, 0x14, 0x0F, 0x05, 0x05, 0x0F, 0x0F, 0x05, 0x0A, 0x05, 0x14, 0x05, 0x0F, 0x14, 0x05, 0x14, 0x14, 0x14, 0x14, 0x0A, 0x14, 0x0A, 0x0F, 0x14, 0x0F, 0x0A, 0x0A, 0x05, 0x0A, 0x05, 0x05, 0x0A, 0x05, 0x05, 0x0A, 0x05, 0x05, 0x05, 0x0F, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0F, 0x14, 0x0F, 0x0A, 0x0F, 0x0A, 0x0F, 0x0A, 0x14, 0x0A, 0x0F, 0x0A, 0x14, 0x14, 0x14, 0x14, 0x14, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x14, 0x0F, 0x0A, 0x0F, 0x0F, 0x0F, 0x0F, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0F, 0x0F, 0x0F, 0x0F, 0x05, 0x05, 0x0F, 0x05, 0x0A, 0x0A, 0x0A, 0x14, 0x14, 0x14, 0x0A, 0x0A, 0x1E, 0x0F, 0x0F, 0x0A, 0x0F, 0x19, 0x0A, 0x14, 0x0A, 0x0A, 0x0A, 0x14, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0F, 0x0F, 0x05, 0x05, 0x0A, 0x0A, 0x0A, 0x05, 0x05, 0x0A, 0x05, 0x05, 0x0F, 0x0A, 0x05, 0x05, 0x05 }

PPVal[0] = 0x00

function rand(seed) -- Thanks Kaphotics
	return (0x4e6d*(seed%65536)+((0x41c6*(seed%65536)+0x4e6d*math.floor(seed/65536))%65536)*65536+0x6073)%4294967296
end

function ReadSeen(offset)
	Seen = 0
	for i = 1, 0x52, 1 do
		if bit.band(memory.readbyte(offset), 0x01) == 0x01 or bit.band(memory.readbyte(offset + 0x54), 0x01) == 0x01 or bit.band(memory.readbyte(offset + 0xA8), 0x01) == 0x01 or bit.band(memory.readbyte(offset + 0xFC), 0x01) == 0x01 then
			Seen = Seen + 1
		end

		if bit.band(memory.readbyte(offset), 0x02) == 0x02 or bit.band(memory.readbyte(offset + 0x54), 0x02) == 0x02 or bit.band(memory.readbyte(offset + 0xA8), 0x02) == 0x02 or bit.band(memory.readbyte(offset + 0xFC), 0x02) == 0x02 then
			Seen = Seen + 1
		end

		if bit.band(memory.readbyte(offset), 0x04) == 0x04 or bit.band(memory.readbyte(offset + 0x54), 0x04) == 0x04 or bit.band(memory.readbyte(offset + 0xA8), 0x04) == 0x04 or bit.band(memory.readbyte(offset + 0xFC), 0x04) == 0x04 then
			Seen = Seen + 1
		end

		if bit.band(memory.readbyte(offset), 0x08) == 0x08 or bit.band(memory.readbyte(offset + 0x54), 0x08) == 0x08 or bit.band(memory.readbyte(offset + 0xA8), 0x08) == 0x08 or bit.band(memory.readbyte(offset + 0xFC), 0x08) == 0x08 then
			Seen = Seen + 1
		end

		if bit.band(memory.readbyte(offset), 0x10) == 0x10 or bit.band(memory.readbyte(offset + 0x54), 0x10) == 0x10 or bit.band(memory.readbyte(offset + 0xA8), 0x10) == 0x10 or bit.band(memory.readbyte(offset + 0xFC), 0x10) == 0x10 then
			Seen = Seen + 1
		end

		if bit.band(memory.readbyte(offset), 0x20) == 0x20 or bit.band(memory.readbyte(offset + 0x54), 0x20) == 0x20 or bit.band(memory.readbyte(offset + 0xA8), 0x20) == 0x20 or bit.band(memory.readbyte(offset + 0xFC), 0x20) == 0x20 then
			Seen = Seen + 1
		end

		if bit.band(memory.readbyte(offset), 0x40) == 0x40 or bit.band(memory.readbyte(offset + 0x54), 0x40) == 0x40 or bit.band(memory.readbyte(offset + 0xA8), 0x40) == 0x40 or bit.band(memory.readbyte(offset + 0xFC), 0x40) == 0x40 then
			Seen = Seen + 1
		end

		if bit.band(memory.readbyte(offset), 0x80) == 0x80 or bit.band(memory.readbyte(offset + 0x54), 0x80) == 0x80 or bit.band(memory.readbyte(offset + 0xA8), 0x80) == 0x80 or bit.band(memory.readbyte(offset + 0xFC), 0x80) == 0x80 then
			Seen = Seen + 1
		end
		
		offset = offset + 1
	end	
end

function ReadOwn(offset)
	Own = 0
	for i = 1, 0x52, 1 do
		if bit.band(memory.readbyte(offset), 0x01) == 0x01 then
			Own = Own + 1
		end

		if bit.band(memory.readbyte(offset), 0x02) == 0x02 then
			Own = Own + 1
		end

		if bit.band(memory.readbyte(offset), 0x04) == 0x04 then
			Own = Own + 1
		end

		if bit.band(memory.readbyte(offset), 0x08) == 0x08 then
			Own = Own + 1
		end

		if bit.band(memory.readbyte(offset), 0x10) == 0x10 then
			Own = Own + 1
		end

		if bit.band(memory.readbyte(offset), 0x20) == 0x20 then
			Own = Own + 1
		end

		if bit.band(memory.readbyte(offset), 0x40) == 0x40 then
			Own = Own + 1
		end

		if bit.band(memory.readbyte(offset), 0x80) == 0x80 then
			Own = Own + 1
		end
		
		offset = offset + 1
	end
end

function ReadParty(offset)
	Valid = true;
	for CurrentPokemon = 1, 6, 1 do
		for i = 1, 220, 1 do
			EncryptedPKMData[i] = memory.readbyte(offset)
			offset = offset + 1
		end
		
		DecryptedPKMData[0x00] = EncryptedPKMData[0x00]
		DecryptedPKMData[0x01] = EncryptedPKMData[0x01]
		DecryptedPKMData[0x02] = EncryptedPKMData[0x02]
		DecryptedPKMData[0x03] = EncryptedPKMData[0x03]
		DecryptedPKMData[0x04] = EncryptedPKMData[0x04]
		DecryptedPKMData[0x05] = EncryptedPKMData[0x05]
		DecryptedPKMData[0x06] = EncryptedPKMData[0x06]
		DecryptedPKMData[0x07] = EncryptedPKMData[0x07]
		DecryptedPKMData[0x08] = EncryptedPKMData[0x08]

		Seed = EncryptedPKMData[7] + bit.lshift(EncryptedPKMData[8], 8)

		for i = 9, 136, 2 do
			EncryptedData = EncryptedPKMData[i] + bit.lshift(EncryptedPKMData[i + 1], 8)
                        Seed = rand(Seed)
			DecryptedData = bit.bxor(EncryptedData, bit.rshift(Seed, 0x10))
			EncryptedPKMData[i] = DecryptedData - bit.lshift(bit.rshift(DecryptedData, 8), 8)
			EncryptedPKMData[i + 1] = bit.rshift(DecryptedData, 8)
		end

		PID = EncryptedPKMData[0x01] + bit.lshift(EncryptedPKMData[0x02], 8) + bit.lshift(EncryptedPKMData[0x03], 16) + bit.lshift(EncryptedPKMData[0x04], 24)
		BlockOrder = bit.band(bit.rshift(PID, 0x0D), 0x1F) % 24

		EncryptedOffset = 0x09
		if BlockOrder == 0 then UnshuffleBlock_A() UnshuffleBlock_B() UnshuffleBlock_C() UnshuffleBlock_D()
		elseif BlockOrder == 1 then UnshuffleBlock_A() UnshuffleBlock_B() UnshuffleBlock_D() UnshuffleBlock_C()
		elseif BlockOrder == 2 then UnshuffleBlock_A() UnshuffleBlock_C() UnshuffleBlock_B() UnshuffleBlock_D()
		elseif BlockOrder == 3 then UnshuffleBlock_A() UnshuffleBlock_C() UnshuffleBlock_D() UnshuffleBlock_B()
		elseif BlockOrder == 4 then UnshuffleBlock_A() UnshuffleBlock_D() UnshuffleBlock_B() UnshuffleBlock_C()
		elseif BlockOrder == 5 then UnshuffleBlock_A() UnshuffleBlock_D() UnshuffleBlock_C() UnshuffleBlock_B()
		elseif BlockOrder == 6 then UnshuffleBlock_B() UnshuffleBlock_A() UnshuffleBlock_C() UnshuffleBlock_D()
		elseif BlockOrder == 7 then UnshuffleBlock_B() UnshuffleBlock_A() UnshuffleBlock_D() UnshuffleBlock_C()
		elseif BlockOrder == 8 then UnshuffleBlock_B() UnshuffleBlock_C() UnshuffleBlock_A() UnshuffleBlock_D()
		elseif BlockOrder == 9 then UnshuffleBlock_B() UnshuffleBlock_C() UnshuffleBlock_D() UnshuffleBlock_A()
		elseif BlockOrder == 10 then UnshuffleBlock_B() UnshuffleBlock_D() UnshuffleBlock_A() UnshuffleBlock_C()
		elseif BlockOrder == 11 then UnshuffleBlock_B() UnshuffleBlock_D() UnshuffleBlock_C() UnshuffleBlock_A()
		elseif BlockOrder == 12 then UnshuffleBlock_C() UnshuffleBlock_A() UnshuffleBlock_B() UnshuffleBlock_D()
		elseif BlockOrder == 13 then UnshuffleBlock_C() UnshuffleBlock_A() UnshuffleBlock_D() UnshuffleBlock_B()
		elseif BlockOrder == 14 then UnshuffleBlock_C() UnshuffleBlock_B() UnshuffleBlock_A() UnshuffleBlock_D()
		elseif BlockOrder == 15 then UnshuffleBlock_C() UnshuffleBlock_B() UnshuffleBlock_D() UnshuffleBlock_A()
		elseif BlockOrder == 16 then UnshuffleBlock_C() UnshuffleBlock_D() UnshuffleBlock_A() UnshuffleBlock_B()
		elseif BlockOrder == 17 then UnshuffleBlock_C() UnshuffleBlock_D() UnshuffleBlock_B() UnshuffleBlock_A()
		elseif BlockOrder == 18 then UnshuffleBlock_D() UnshuffleBlock_A() UnshuffleBlock_B() UnshuffleBlock_C()
		elseif BlockOrder == 19 then UnshuffleBlock_D() UnshuffleBlock_A() UnshuffleBlock_C() UnshuffleBlock_B()
		elseif BlockOrder == 20 then UnshuffleBlock_D() UnshuffleBlock_B() UnshuffleBlock_A() UnshuffleBlock_C()
		elseif BlockOrder == 21 then UnshuffleBlock_D() UnshuffleBlock_B() UnshuffleBlock_C() UnshuffleBlock_A()
		elseif BlockOrder == 22 then UnshuffleBlock_D() UnshuffleBlock_C() UnshuffleBlock_A() UnshuffleBlock_B()
		elseif BlockOrder == 23 then UnshuffleBlock_D() UnshuffleBlock_C() UnshuffleBlock_B() UnshuffleBlock_A()
		end

		Seed = PID
		for i = 137, 220, 2 do
			EncryptedData = EncryptedPKMData[i] + bit.lshift(EncryptedPKMData[i + 1], 8)
                        Seed = rand(Seed)
			DecryptedData = bit.bxor(EncryptedData, bit.rshift(Seed, 0x10))
			DecryptedPKMData[i] = DecryptedData - bit.lshift(bit.rshift(DecryptedData, 8), 8)
			DecryptedPKMData[i + 1] = bit.rshift(DecryptedData, 8)
		end

		Checksum = 0
		for i = 9, 136, 2 do
			Checksum = Checksum + DecryptedPKMData[i] + bit.lshift(DecryptedPKMData[i + 1], 8)
			Checksum = bit.band(Checksum, 0xFFFF)
		end

		if Checksum == DecryptedPKMData[0x07] + bit.lshift(DecryptedPKMData[0x08], 8) then	
			ID[CurrentPokemon] = DecryptedPKMData[0x09] + bit.lshift(DecryptedPKMData[0x0A], 8)
			Move1[CurrentPokemon] = DecryptedPKMData[0x29] + bit.lshift(DecryptedPKMData[0x2A], 8)
			Move2[CurrentPokemon] = DecryptedPKMData[0x2B] + bit.lshift(DecryptedPKMData[0x2C], 8)
			Move3[CurrentPokemon] = DecryptedPKMData[0x2D] + bit.lshift(DecryptedPKMData[0x2E], 8)
			Move4[CurrentPokemon] = DecryptedPKMData[0x2F] + bit.lshift(DecryptedPKMData[0x30], 8)
			PP1[CurrentPokemon] = DecryptedPKMData[0x31]
			PP2[CurrentPokemon] = DecryptedPKMData[0x32]
			PP3[CurrentPokemon] = DecryptedPKMData[0x33]
			PP4[CurrentPokemon] = DecryptedPKMData[0x34]
			
			if PPVal[Move1[CurrentPokemon]] ~= nil then	
				MAXPP1[CurrentPokemon] = PPVal[Move1[CurrentPokemon]] * (1.0 + (DecryptedPKMData[0x35] * 0.2))
			else
				MAXPP1[CurrentPokemon] = MAXPP1_2[CurrentPokemon]
			end
			if PPVal[Move2[CurrentPokemon]] ~= nil then	
				MAXPP2[CurrentPokemon] = PPVal[Move2[CurrentPokemon]] * (1.0 + (DecryptedPKMData[0x36] * 0.2))
			else
				MAXPP2[CurrentPokemon] = MAXPP2_2[CurrentPokemon]
			end
			if PPVal[Move3[CurrentPokemon]] ~= nil then	
				MAXPP3[CurrentPokemon] = PPVal[Move3[CurrentPokemon]] * (1.0 + (DecryptedPKMData[0x37] * 0.2))
			else
				MAXPP3[CurrentPokemon] = MAXPP3_2[CurrentPokemon]
			end
			if PPVal[Move4[CurrentPokemon]] ~= nil then	
				MAXPP4[CurrentPokemon] = PPVal[Move4[CurrentPokemon]] * (1.0 + (DecryptedPKMData[0x38] * 0.2))
			else
				MAXPP4[CurrentPokemon] = MAXPP4_2[CurrentPokemon]
			end

			Egg[CurrentPokemon] = bit.rshift(bit.band(DecryptedPKMData[0x3C], 0x40), 0x06)
			Gender[CurrentPokemon] = bit.rshift(bit.band(DecryptedPKMData[0x41], 0x06), 0x01) 
			Status[CurrentPokemon] = DecryptedPKMData[0x89]
			HP[CurrentPokemon] = DecryptedPKMData[0x8F] + bit.lshift(DecryptedPKMData[0x90], 8)
			MAXHP[CurrentPokemon] = DecryptedPKMData[0x91] + bit.lshift(DecryptedPKMData[0x92], 8)
			Lvl[CurrentPokemon] = DecryptedPKMData[0x8D]
		
			if HP[CurrentPokemon] > 714 or MAXHP[CurrentPokemon] > 714 or Lvl[CurrentPokemon] > 100 then
				Valid = false
			end
		else
			Valid = false
		end	
	end

	if Valid then
		for CurrentPokemon = 1, 6, 1 do
			ID2[CurrentPokemon] = ID[CurrentPokemon]
			Move1_2[CurrentPokemon] = Move1[CurrentPokemon]
			Move2_2[CurrentPokemon] = Move2[CurrentPokemon]
			Move3_2[CurrentPokemon] = Move3[CurrentPokemon]
			Move4_2[CurrentPokemon] = Move4[CurrentPokemon]
			PP1_2[CurrentPokemon] = PP1[CurrentPokemon]
			PP2_2[CurrentPokemon] = PP2[CurrentPokemon]
			PP3_2[CurrentPokemon] = PP3[CurrentPokemon]
			PP4_2[CurrentPokemon] = PP4[CurrentPokemon]
			MAXPP1_2[CurrentPokemon] = MAXPP1[CurrentPokemon]
			MAXPP2_2[CurrentPokemon] = MAXPP2[CurrentPokemon]
			MAXPP3_2[CurrentPokemon] = MAXPP3[CurrentPokemon]
			MAXPP4_2[CurrentPokemon] = MAXPP4[CurrentPokemon]
			Egg2[CurrentPokemon] = Egg[CurrentPokemon]
			Gender2[CurrentPokemon] = Gender[CurrentPokemon]
			Status2[CurrentPokemon] = Status[CurrentPokemon]
			HP2[CurrentPokemon] = HP[CurrentPokemon]
			MAXHP2[CurrentPokemon] = MAXHP[CurrentPokemon]
			Lvl2[CurrentPokemon] = Lvl[CurrentPokemon]
		end
	end
end

function UnshuffleBlock_A()
	DecryptedOffset = 0x09;
	for i = 1, 32, 1 do
		DecryptedPKMData[DecryptedOffset] = EncryptedPKMData[EncryptedOffset]
		EncryptedOffset = EncryptedOffset + 1
		DecryptedOffset = DecryptedOffset + 1
	end
end

function UnshuffleBlock_B()
	DecryptedOffset = 0x29;
	for i = 1, 32, 1 do
		DecryptedPKMData[DecryptedOffset] = EncryptedPKMData[EncryptedOffset]
		EncryptedOffset = EncryptedOffset + 1
		DecryptedOffset = DecryptedOffset + 1
	end
end

function UnshuffleBlock_C()
	DecryptedOffset = 0x49;
	for i = 1, 32, 1 do
		DecryptedPKMData[DecryptedOffset] = EncryptedPKMData[EncryptedOffset]
		EncryptedOffset = EncryptedOffset + 1
		DecryptedOffset = DecryptedOffset + 1
	end
end

function UnshuffleBlock_D()
	DecryptedOffset = 0x69;
	for i = 1, 32, 1 do
		DecryptedPKMData[DecryptedOffset] = EncryptedPKMData[EncryptedOffset]
		EncryptedOffset = EncryptedOffset + 1
		DecryptedOffset = DecryptedOffset + 1
	end
end

function ReadBadgeSet(badge)
	if bit.band(badge, 0x01) == 0x01 then
		BadgeData[1] = 0x01
	else
		BadgeData[1] = 0x00
	end

	if bit.band(badge, 0x02) == 0x02 then
		BadgeData[2] = 0x01
	else
		BadgeData[2] = 0x00
	end

	if bit.band(badge, 0x04) == 0x04 then
		BadgeData[3] = 0x01
	else
		BadgeData[3] = 0x00
	end

	if bit.band(badge, 0x08) == 0x08 then
		BadgeData[4] = 0x01
	else
		BadgeData[4] = 0x00
	end

	if bit.band(badge, 0x10) == 0x10 then
		BadgeData[5] = 0x01
	else
		BadgeData[5] = 0x00
	end

	if bit.band(badge, 0x20) == 0x20 then
		BadgeData[6] = 0x01
	else
		BadgeData[6] = 0x00
	end

	if bit.band(badge, 0x40) == 0x40 then
		BadgeData[7] = 0x01
	else
		BadgeData[7] = 0x00
	end

	if bit.band(badge, 0x80) == 0x80 then
		BadgeData[8] = 0x01
	else
		BadgeData[8] = 0x00
	end
end

for i = 1, 6, 1 do
	ID2[i] = 0
	Move1_2[i] = 0
	Move2_2[i] = 0
	Move3_2[i] = 0
	Move4_2[i] = 0
	PP1_2[i] = 0
	PP2_2[i] = 0
	PP3_2[i] = 0
	PP4_2[i] = 0
	MAXPP1_2[i] = 0
	MAXPP2_2[i] = 0
	MAXPP3_2[i] = 0
	MAXPP4_2[i] = 0
	Egg2[i] = 0
	Gender2[i] = 0
	Status2[i] = 0
	HP2[i] = 0
	MAXHP2[i] = 0
	Lvl2[i] = 0
end

Seen = 0
Own = 0

while true do
	if emu.framecount() % 30 == 1 then
		BadgeData[1] = 0
		BadgeData[2] = 0
		BadgeData[3] = 0
		BadgeData[4] = 0
		BadgeData[5] = 0
		BadgeData[6] = 0
		BadgeData[7] = 0
		BadgeData[8] = 0
		PartyOffset = 0
		BattleOffset = 0
		SeenOffset = 0
		OwnOffset = 0
		Money = 0
		BadgeSet = 0
		MapID = 0
		if memory.readdword(0x02FFFE0C) == 0x4F425249 or memory.readdword(0x02FFFE0C) == 0x4F415249  then --B/W
			if memory.readdword(0x02000024) ~= 0x00 then
				PartyOffset = memory.readdword(0x02000024) + 0x196BC
				BattleOffset = memory.readdword(0x02000024) + 0x4EF3C
				SeenOffset = memory.readdword(0x02000024) + 0x21F18
				OwnOffset = memory.readdword(0x02000024) + 0x21EC4
				Money = memory.readdword(memory.readdword(0x02000024) + 0x21ABC)
				BadgeSet = memory.readbyte(memory.readdword(0x02000024) + 0x21AC0)
				MapID = memory.readword(memory.readdword(0x02000024) + 0x3461C)
			end
		elseif memory.readdword(0x02FFFE0C) == 0x4F455249 or memory.readdword(0x02FFFE0C) == 0x4F445249 then --B2/W2
			if memory.readdword(0x02111880) ~= 0x00 then
				PartyOffset = memory.readdword(0x02000024) + 0x19720
				BattleOffset = memory.readdword(0x02000024) + 0x530A8
				SeenOffset = memory.readdword(0x02000024) + 0x21D7C
				OwnOffset = memory.readdword(0x02000024) + 0x21D28
				Money = memory.readdword(memory.readdword(0x02000024) + 0x21A20)
				BadgeSet = memory.readbyte(memory.readdword(0x02000024) + 0x21A24)
				MapID = memory.readword(memory.readdword(0x02000024) + 0x36780)
			end
		end

		if BattleOffset ~= 0x00 then
			if memory.readdword(BattleOffset) == 0x06 then
				ReadParty(BattleOffset + 0x08)
			elseif PartyOffset ~= 0x00 then
				if memory.readdword(PartyOffset) == 0x06 then
					ReadParty(PartyOffset + 0x08)
				end
			end
		end

		if SeenOffset ~= 0x00 then
			ReadSeen(SeenOffset)
		end

		if OwnOffset ~= 0x00 then
			ReadOwn(OwnOffset)
		end

		ReadBadgeSet(BadgeSet)
		
		print(MapID)
		print("\n")

		for i = 1, 8, 1 do
			print(string.format("Badge%d = %d", i, BadgeData[i]))
			print("\n")
		end

		print(string.format("Money = %d", Money, "\n"))
		print("\n")

		print(string.format("Seen = %d", Seen, "\n"))
		print("\n")

		print(string.format("Own = %d", Own, "\n"))
		print("\n")

		for i = 1, 6, 1 do
			file:write(string.format("PKM%d = %d, Gender = %d,  HP = %d, MAXHP = %d, Lvl = %d, Status = %d, Egg = %d", i, ID2[i], Gender2[i], HP2[i], MAXHP2[i], Lvl2[i], Status2[i], Egg2[i], "\n"))
			file:write("\n")
			file:write(string.format("Move1 = %d %d/%d, Move2 = %d %d/%d, Move3 = %d %d/%d, Move4 = %d %d/%d", Move1_2[i], PP1_2[i], MAXPP1_2[i], Move2_2[i], PP2_2[i], MAXPP2_2[i], Move3_2[i], PP3_2[i], MAXPP3_2[i], Move4_2[i], PP4_2[i], MAXPP4_2[i], "\n"))
			file:write("\n")
			file:write("\n")
				
		end
		
		
		

		--Egg
		--0x00 = Not Egg
		--0x01 = Is Egg

		--Gender
		--0x00 = Male
		--0x01 = Female
		--0x02 = Genderless

		--Status
		--0x00 = Healthy
		--0x01 to 0x07 Sleeping, each turn it is reduced by 1. when it is 0x01 it means it will wake that turn.
		--0x08 = Poisoned
		--0x10 = Burned
		--0x20 = Frozen
		--0x40 = Paralyzed
		--0x80 = Toxic
		file:close()
		file = assert(io.open("team.txt", "w"))
	end
	emu.frameadvance()

end