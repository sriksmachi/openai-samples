/****** Object:  Table [dbo].[flights]    Script Date: 7/28/2023 11:48:19 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].[flights]

CREATE TABLE [dbo].[flights](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[source] [nvarchar](50) NULL,
	[destination] [nvarchar](50) NULL,
	[price] [int] NULL,
	[departure] [nvarchar](50) NULL,
	[arrival] [nvarchar](50) NULL,
	[numberofstops] [nvarchar](50) NULL,
	[date] [nvarchar](50) NULL,
 CONSTRAINT [PK_flights] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

-- Create insert scripts for flights table
-- Path: complete-ai-app\infra\flights.sql
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Bangalore','Goa',2500,'10:00','12:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Bangalore','Goa',1500,'6:00','7:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Goa','Hyderabad',3600,'10:00','12:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Goa','Hyderabad',4600,'15:00','16:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Hyderabad','Bangalore',3700,'11:00','12:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Hyderabad','Bangalore',4700,'16:00','17:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Bangalore','Hyderabad',4800,'10:00','12:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Bangalore','Hyderabad',5800,'21:00','22:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Hyderabad','Goa',2900,'10:00','12:00','0','2023-07-28')
INSERT INTO [dbo].[flights] ([source],[destination],[price],[departure],[arrival],[numberofstops],[date]) VALUES ('Hyderabad','Goa',3900,'20:00','21:00','0','2023-07-28')

 
 